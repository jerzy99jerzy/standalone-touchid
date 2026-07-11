# 1. Protocol analysis — Apple's Touch ID cryptographic architecture

Understanding the Touch ID protocol matters for two reasons: it explains why this build works at all without electronic modification, and it defines the threat model and operational constraints (re-pairing when moving to a new Mac, no concurrent use with multiple Macs).

## 1.1 Layer architecture

Magic Keyboard with Touch ID does not store biometric templates or perform matching. It is a sensor. All logic — enrollment, matching, policy enforcement (48-hour password requirement, failed-attempt lockouts) — runs inside the Secure Enclave on your Mac. Communication between the sensor and the Secure Enclave crosses two critical secured channels stacked in series.

## 1.2 Channel 1 — sensor to PKA block (inside the keyboard)

The keyboard contains a dedicated Public Key Accelerator (PKA) block that sits between the fingerprint sensor and the outside world. The secure channel between the sensor and its PKA block is established at manufacture using a unique key shared between the two components. This is the same technique used in MacBooks with integrated Touch ID, where the secure channel exists between the built-in sensor and the Secure Enclave. Raw sensor data never leaves the keyboard in plaintext.

## 1.3 Channel 2 — PKA block to Mac Secure Enclave

The keyboard must be paired with a specific Mac before any biometric operation. Apple performs this pairing at the factory for keyboards shipped bundled with a Mac. User-initiated pairing is also supported, which is what this project relies on — you are working with a keyboard that was likely paired to someone else's Mac before you got it.

A keyboard is paired to exactly one Mac at any time. A single Mac can maintain pairings with up to five keyboards simultaneously.

### Pairing handshake

The Secure Enclave on the Mac and the PKA block in the keyboard exchange public keys rooted in a trusted Apple certificate authority. They use hardware-held attestation keys along with Ephemeral Elliptic Curve Diffie-Hellman (ECDHE) to mutually attest identity. Mac-side state is held by the Secure Enclave; keyboard-side by the PKA block. Attestation rooted in Apple's CA is what defeats the supply-chain attack of substituting a counterfeit keyboard — the Secure Enclave will refuse to pair with anything that cannot present a valid Apple-signed attestation.

## 1.4 Runtime session

After pairing, the runtime session is conventional authenticated encryption: all Touch ID data between the Mac and the keyboard is encrypted with AES-GCM using 256-bit keys, with ephemeral ECDH keys on the NIST P-256 curve derived from the stored pairing identities.

The transport layer — Lightning cable in this project, wired connection — is not part of the trust chain. The cable is a dumb carrier for ciphertext. Owning the transport layer gives an attacker encrypted data only.

## 1.5 Secure intent

Cryptography alone does not defeat local malware-driven "press it for me" attacks. Apple adds a physical-intent gate for sensitive operations. First-time use of high-privilege actions such as enrolling a new fingerprint requires either:

- A double-press of the Mac's power button, or
- A successful match against a previously enrolled fingerprint.

For Apple Pay, authorization requires either a Touch ID match, or the macOS user password combined with a double-press of the Touch ID button on the keyboard. The second option is a way to express physical intent without providing biometrics. Both flows route through the Secure Enclave's secure intent path, which software running on the Application Processor cannot forge.

## 1.6 Implications for this build

Because the sensor, the PKA block, and the logic board all remain physically intact in this project — only the mechanical enclosure is replaced — the device retains every property described above. macOS recognizes it as a legitimate Magic Keyboard with Touch ID.

You perform pairing once at first connection, enroll a fingerprint identically to a factory keyboard, and use it identically to the built-in Touch ID on a MacBook.

## References

- [Apple Platform Security — Magic Keyboard with Touch ID](https://support.apple.com/guide/security/magic-keyboard-with-touch-id-secf60513daa/web)
- [Apple Platform Security — Biometric security](https://support.apple.com/guide/security/biometric-security-sec067eb0c9e/web)
- [Apple Platform Security — Secure intent and connections to the Secure Enclave](https://support.apple.com/guide/security/secure-intent-connections-enclave-sec7a94f7d1e/web)
