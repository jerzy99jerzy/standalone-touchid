# 9. Threat model and security notes

This build preserves Apple's original cryptographic stack: the sensor, the PKA block, and the logic board are carried over physically unmodified, and only the mechanical housing is replaced. The security posture is therefore close to that of a factory Magic Keyboard with Touch ID, and the interesting work is in the word "close". Five attack classes come out identical. One does not, and it is not a cryptographic one.

Claims below are attributed. Where this document reasons past what Apple or the upstream builders state, it says so.

## 9.1 Transport attacks (the cable)

AES-GCM with a 256-bit key and ephemeral P-256 keys protects traffic between the PKA block and the Secure Enclave, per Apple's Platform Security guide. An attacker holding the cable, whether through an in-line tap or a dock with MITM capability, sees authenticated ciphertext and traffic metadata.

No publicly documented practical attack exists at this layer. That is a weaker statement than "no attack is possible", and it is the one the evidence supports.

## 9.2 Supply chain and the used donor

This is the one risk class the build genuinely adds, and it comes from procurement rather than from cryptography.

**What attestation covers.** Pairing requires the keyboard's PKA block to present an attestation rooted in Apple's certificate authority. A counterfeit device, or a substituted sensor, cannot negotiate that handshake without Apple's CA private keys. The classic swap-the-hardware attack is closed at the protocol level, and this build does nothing to weaken it, because the PKA block and its keys are exactly the ones that left the factory.

**What attestation does not cover.** Attestation authenticates the biometric channel. It says nothing about the rest of the device. The donor logic board comes across whole, and *[inference, not verified against a built unit]* its HID keyboard interface is expected to remain present even after the key matrix is discarded. A donor carrying an implant on that path would be a keystroke injection surface, and no part of the Touch ID protocol would notice, because HID is not in the attested channel. The attack requires an adversary who controls a device before you buy it, which is a narrow scenario for a random marketplace purchase and a much less narrow one if you are a person worth targeting.

**What follows in practice:**

- Buy from sellers with history and a return path. On a device whose whole function is authorization, price is the wrong variable to optimise.
- Model number and port must agree. The generations carry disjoint model numbers (see [requirements 3.1](03-requirements.md)), so a listing that says A2449 while showing a USB-C port describes hardware it does not have. Walk away rather than investigate.
- Inspect the adhesive seam before buying where you can, and before opening where you cannot. Factory bonding is uniform; a previous entry usually shows at the edges.
- You are going to open the device anyway, which is a tamper inspection nobody buying a factory keyboard gets. Photograph the internals before touching anything and compare against the teardown references in [Credits](../CREDITS.md).
- After assembly, confirm what actually enumerates before you enrol a fingerprint. Procedure in [pairing 8.6](08-pairing.md#86-verifying-what-you-built).

## 9.3 Liveness and presentation attacks

The Touch ID sensor images subdermal ridge structure capacitively rather than photographing the surface of the finger, which is why photographs and crude silicone lifts do not work against it. Apple describes the sensor this way, and the property is a function of the sensor hardware, so it carries over into this build unchanged.

Be careful about how far that gets stated. Capacitive fingerprint sensors, Apple's included, have been defeated in laboratory conditions by researchers working from a lifted print and a well-made mould, most famously against the first-generation Touch ID in 2013. Apple publishes no presentation-attack-detection rating for this sensor. The honest claim is that Touch ID resists opportunistic presentation attacks and has a documented history of falling to determined, well-resourced ones. Nothing in this build changes either half of that, in any direction.

## 9.4 Local malware-driven authorization

The secure intent gate protects against a malicious process on the Mac authorizing `sudo` or Apple Pay programmatically. The button press reaches the Secure Enclave over a hardware path the Application Processor cannot drive or forge, so there is no virtual button to press. One physical touch, one authorization.

This build carries over the original button and its connection to the logic board, so the same signal path does the same job.

## 9.5 Physical desk access

Someone with physical access to both your Mac and the device can authorize actions if they have a fingerprint enrolled on that Mac. The protection here is real but bounded: an authorization needs a finger that was previously enrolled, present at the sensor. It is not a protection against anyone whose finger is already in the list.

That list is the part people forget. A fingerprint you enrolled for a partner or family member stays valid until you delete it, and nothing prompts you to revisit the decision.

**Mitigation:** System Settings, Touch ID & Password, lists enrolled fingerprints individually and lets you delete them one at a time. Audit it on a schedule rather than when you happen to think of it.

## 9.6 Build-specific risks

Three risk classes come out of the mechanical work. None of them is a security failure; they are ways to end up with an expensive paperweight.

**Flex cable damage during teardown.** Shows up as macOS never seeing the device. Nothing is compromised, the device is simply dead. Mitigation is care, per [section 6](06-teardown.md).

**Improper back plate torque.** The spring plate ends up under-compressed and the button either false-triggers or fails to register. Annoying, not dangerous.

**No ESD protection during assembly.** The logic board has ESD-sensitive components on it. Wrist strap, mat, and not working on synthetic carpet. Note that the electrical tape in [assembly step 9](07-assembly.md) is short-circuit insurance and does nothing for ESD; these are separate problems.

## 9.7 Outside the boundary

What a Touch ID authenticator does not address, in this build or any other:

- **Coerced authentication.** Someone with physical access to you and to the device can make you press the button. Touch ID is a convenience mechanism for a legitimate user, not a defence against duress. This is the limit that [9.5](#95-physical-desk-access) runs into.
- **macOS compromised below the prompt.** If the Secure Enclave on your Mac is compromised, which is hard but not categorically impossible for a well-resourced attacker, enrolled templates are exposed. Nothing at the keyboard end helps.
- **Loss of the paired Mac.** The box is worthless to whoever finds the Mac, because the pairing is bound to that Mac's Secure Enclave. It is equally unusable to you elsewhere until you re-pair it.
- **Rubber-hose cryptanalysis.** The standard XKCD 538 caveat, which is really just [9.7](#97-outside-the-boundary)'s first bullet with a picture attached.

## 9.8 Summary posture

For a personal workstation used by one person, or by a household of people you would hand your password to anyway, this build is equivalent to a factory Apple keyboard on every attack class in this document except one. The exception is donor provenance, and it is mitigated by where you buy and by looking at what you built rather than by anything cryptographic.

For high-security or regulated environments, the question is not technical. Many such environments reject physically modified hardware categorically, regardless of what survived the modification, and they are not wrong to have a bright-line rule there. Check the policy before you build, not after.
