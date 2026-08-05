# 1. Protocol analysis: Apple's Touch ID cryptographic architecture

Understanding the Touch ID protocol matters for two reasons. It explains why this build works at all without electronic modification, and it defines the threat model and operational constraints (re-pairing when moving to a new Mac, no concurrent use with multiple Macs). This section is longer than a build guide strictly needs, because the whole premise of the project rests on one claim: that rehousing the electronics changes nothing the Secure Enclave cares about. That claim deserves to be justified in detail rather than asserted.

Everything in this section is sourced from Apple's Platform Security guide. Where this document draws a conclusion Apple does not state directly, it is labeled as inference.

## 1.1 The separation-of-responsibilities model

Apple's biometric architecture rests on a strict division of labor between the sensor and the Secure Enclave, connected by a secured channel. The sensor captures the biometric image and transmits it. The Secure Enclave does everything else: during enrollment it processes, encrypts, and stores the template data; during matching it compares incoming sensor data against the stored templates and returns only a yes/no result.

Magic Keyboard with Touch ID does not store biometric templates, does not perform matching, and does not enforce security policy (the 48-hour password requirement, failed-attempt lockouts). It is a sensor and nothing more. All of that logic runs inside the Secure Enclave on your Mac, exactly as it would for a Touch ID sensor built into a MacBook.

This is the architectural fact that makes the project possible. Because the intelligence lives in the Mac and the keyboard is a dumb (but cryptographically authenticated) capture device, moving the sensor into a different physical housing is invisible to the Secure Enclave. You are not modifying anything the security model depends on. You are re-housing a peripheral.

### Template handling detail

The template never contains a reconstructable fingerprint. When the sensor scans a finger, it produces a raster scan (historically an 88x88 pixel, 500 ppi image on early sensors). That raster is vectorized inside the Secure Enclave, stored temporarily in encrypted memory, and then discarded. The analysis uses subdermal ridge-flow angle mapping, a deliberately lossy process that throws away the "finger minutiae data" that would be needed to reconstruct the actual print. What remains is a map of nodes, stored encrypted, readable only by the Secure Enclave, with no identity information attached. This data never leaves the device, is never sent to Apple, and is not included in backups.

Practical consequence for this build: your enrolled templates live in your Mac's Secure Enclave, not in the keyboard. If you re-pair the box to a different Mac, you enroll again from scratch on that Mac. Nothing about your fingerprints is carried inside the puck.

## 1.2 Two channels in series

The path from fingertip to match decision crosses two independently secured cryptographic channels stacked in series. Both must be intact for the device to function, and both are established at manufacture, which is why you cannot build one of these from non-Apple parts.

```
  +----------+   Channel 1     +-----------+   Channel 2     +----------------+
  | Touch ID |  factory-keyed  | PKA block |  ECDHE-paired   | Secure Enclave |
  |  sensor  |---------------->| (keyboard)|---------------->|   (your Mac)   |
  +----------+  sensor<->PKA    +-----------+  PKA<->SE,       +----------------+
       |                             |         AES-GCM P-256          |
   captures                     attestation                      enrollment,
   raster scan                  + transport                      matching,
                                crypto                           policy
```

## 1.3 Channel 1: sensor to PKA block (inside the keyboard)

The keyboard contains a dedicated hardware Public Key Accelerator (PKA) block sitting between the fingerprint sensor and the outside world. The secure channel between the sensor and its PKA block is established at the factory using a unique key shared between the two components. For Macs with built-in Touch ID, this is the identical technique used to secure the channel between the Secure Enclave and its built-in sensor.

Raw sensor data never leaves the keyboard in plaintext. An attacker tapping the internal flex cable between the sensor and the PKA block sees only encrypted traffic keyed by a factory secret that is not extractable without physically compromising the silicon.

This is also why a counterfeit or tampered sensor cannot be substituted: the shared key was burned in at manufacture, and a replacement sensor has no way to negotiate this channel.

## 1.4 Channel 2: PKA block to Mac Secure Enclave

The keyboard must be paired to a specific Mac before any biometric operation. Apple performs this pairing at the factory for keyboards bundled with a Mac. User-initiated pairing is also supported, which is the path this project relies on, because the donor keyboard was almost certainly paired to someone else's Mac before you acquired it.

A keyboard is paired to exactly one Mac at a time. A single Mac can maintain pairings with up to five keyboards simultaneously. There is no equivalent of Activation Lock on these keyboards; pairing identity is freely cyclable, which is what makes buying a used unit viable.

### The pairing handshake

To pair, the Secure Enclave on the Mac and the PKA block in the keyboard exchange public keys rooted in the trusted Apple certificate authority (CA). They use hardware-held attestation keys together with Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) to mutually attest to their identities. On the Mac, this state is protected by the Secure Enclave; on the keyboard, by the PKA block.

The security-critical element here is attestation rooted in Apple's CA. This is what defeats the supply-chain attack of substituting a counterfeit keyboard with a tampered sensor. The Secure Enclave will refuse to pair with any device that cannot present a valid Apple-signed attestation. An attacker cannot fabricate a keyboard that presents valid attestation without Apple's CA private keys.

Inference: for this build, the attestation model means a home-built puck is only as trustworthy as the donor keyboard's PKA block, which is genuine Apple silicon carried over intact. You are not weakening attestation, because you never touch the PKA block or its keys. This is the crux of why the rehousing is cryptographically transparent.

## 1.5 Runtime session encryption

After pairing, all Touch ID data communicated between the Mac and the keyboard is encrypted with AES-GCM using a 256-bit key, with ephemeral ECDH keys on the NIST P-256 curve derived from the stored pairing identities.

This is worth stating precisely, because it is a point where a careless writer would conflate two different mechanisms. Apple uses different transport crypto for the two sensor topologies:

| Sensor topology | Session key exchange | Transport encryption |
|-----------------|----------------------|----------------------|
| Built-in Touch ID (MacBook; also Magic Keyboard sensor to its own PKA) | AES key wrapping, both sides contributing random | **AES-CCM** |
| Magic Keyboard PKA block to Mac Secure Enclave (Channel 2) | ECDHE, keys rooted in Apple CA | **AES-GCM, 256-bit, ephemeral ECDH P-256** |

Both AES-CCM and AES-GCM are authenticated-encryption (AEAD) modes providing confidentiality and integrity together. The peripheral channel uses GCM; the built-in and sensor-local channel uses CCM. If you see this project (or any writeup) claim the Magic Keyboard uses AES-CCM end to end, that is the built-in channel's cipher being misattributed to the peripheral channel.

The transport layer itself (the Lightning cable in this build, or Bluetooth in wireless mode) is not part of the trust chain. The cable is a dumb carrier for ciphertext. Owning the transport gives an attacker authenticated ciphertext and traffic metadata, nothing more. In Bluetooth mode the same AES-GCM envelope applies on top of the Bluetooth link; compromising the BT stack yields ciphertext.

## 1.6 Secure intent

Cryptography alone does not defeat a local malware-driven "press it for me" attack, where malicious software on the Mac tries to trigger an authorization programmatically. Apple adds a physical-intent gate for sensitive operations.

First-time use of high-privilege actions such as enrolling a new fingerprint requires physical confirmation of intent, expressed in one of two ways:

- A double-press of the Mac's power button when the user interface indicates it, or
- A successful match against a fingerprint previously enrolled with that Mac.

For Apple Pay, authorization is either a Touch ID match, or the macOS user password combined with a double-press of the Touch ID button on the keyboard. The second option lets the user express physical intent without providing biometrics.

Both flows route through the Secure Enclave's secure intent path. Secure intent is a dedicated hardware signaling mechanism: the button-press signal reaches the Secure Enclave over a path that software running on the Application Processor cannot drive or forge. This is what makes "malware presses the virtual button" a non-attack; there is no virtual button, only a hardware line into the SE.

For this build, secure intent is preserved because you carry over the genuine button hardware and its connection to the logic board. The re-housed button drives the same secure-intent signal it did in the original keyboard.

## 1.7 Implications for this build

Putting the pieces together:

- The sensor, the PKA block, and the logic board all remain physically intact. Only the mechanical enclosure is replaced.
- Channel 1 (sensor to PKA) is factory-keyed and untouched.
- Channel 2 (PKA to Secure Enclave) re-attests and re-establishes at pairing time, using keys and attestation you never modify.
- Secure intent is carried by the original button hardware.

The device therefore retains every property described above, and macOS recognizes it as a legitimate Magic Keyboard with Touch ID. You pair once at first connection, enroll a fingerprint identically to a factory keyboard, and use it identically to the built-in Touch ID on a MacBook.

The one property you do change is physical: the sensor is now under a 3D-printed surface with a different mechanical click path. That affects ergonomics and durability (see the [assembly](07-assembly.md) and [teardown](06-teardown.md) sections), not security.

## 1.8 What the protocol does not protect (forward reference)

The cryptographic architecture is strong against remote and transport attackers. It says nothing about an attacker with your enrolled finger, an attacker who can coerce you, or an attacker who has compromised macOS itself at a level below the authorization prompt. Those live in the [threat model](09-threat-model.md), which builds directly on this section.

## References

- [Apple Platform Security: Magic Keyboard with Touch ID](https://support.apple.com/guide/security/magic-keyboard-with-touch-id-secf60513daa/web)
- [Apple Platform Security: Biometric security](https://support.apple.com/guide/security/biometric-security-sec067eb0c9e/web)
- [Apple Platform Security: The Secure Enclave](https://support.apple.com/guide/security/the-secure-enclave-sec59b0b31ff/web)
- [Apple Platform Security: Secure intent and connections to the Secure Enclave](https://support.apple.com/guide/security/secure-intent-connections-enclave-sec7a94f7d1e/web)
- [Apple Support: About Touch ID advanced security technology](https://support.apple.com/en-us/105095)
