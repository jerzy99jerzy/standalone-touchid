# 9. Threat model and security notes

Because this build preserves Apple's full original cryptographic stack — sensor, PKA block, and logic board are physically unmodified — the security posture is functionally identical to a factory Magic Keyboard with Touch ID. Brief review by threat category.

## 9.1 Transport attacks (Lightning cable)

AES-GCM 256-bit with ephemeral P-256 keys protects communication between the PKA block and the Secure Enclave. An attacker with access to the cable (in-line tap, malicious USB-C dock with MITM capability) sees only ciphertext and metadata. No practical attack at this layer.

## 9.2 Hardware supply-chain attacks

This build preserves attestation rooted in Apple's CA. A counterfeit keyboard (substituted by an attacker with physical access) will not pair with your Mac — the Secure Enclave rejects pairing without valid Apple-signed attestation. Supply-chain attack blocked at the pairing protocol level.

Note: this assumes you obtained the donor keyboard from a legitimate source. If the used keyboard you purchased came from an adversary, all bets are off. Buy from reputable secondhand sources; visually inspect for tampering signs (prior openings show at the edge glue).

## 9.3 Liveness and presentation attacks

The Touch ID sensor uses capacitive imaging with liveness detection — it requires live tissue and does not respond to classic fingerprint mold attacks with silicone or photographs. This is a sensor property, not a protocol property, and remains unchanged in this build.

## 9.4 Local malware-driven authorization

The secure intent gate (physical press) protects against a malicious process on the Mac programmatically authorizing `sudo` or Apple Pay. One physical touch equals one authorization. There is no way around this without physical access to the device.

## 9.5 Physical desk access — residual risk

A person with physical access to your device and your Mac can authorize actions if they have an enrolled fingerprint. Your fingerprints are absolutely protected (there is no way to force authorization without your finger present), but if you previously enrolled another person's fingerprint (partner, family member) that person retains permanent authorization until you delete their template from System Settings.

**Mitigation:** the Touch ID & Password panel allows listing and deleting individual fingerprints. Audit the enrolled list every 6 months.

## 9.6 Build-specific risks

Three risk classes emerge from the mechanical modification (electronics remain untouched):

**Ribbon cable damage during teardown:** manifests as macOS not recognizing the device. No compromise of security, just a brick. Mitigation: careful teardown per [section 6](06-teardown.md).

**Improper back plate torque:** the spring plate may be under-compressed, causing the button to false-trigger or fail to register presses. No compromise of security.

**No ESD protection during assembly:** the logic board contains ESD-sensitive components. Mitigation: ESD wrist strap, ESD mat, work in a low-static environment (not on a synthetic carpet).

## 9.7 What this device does not protect against

For completeness — what remains outside the boundary of a Touch ID authenticator:

- **Coerced authentication.** A person with physical access to you and the device can force you to press the button. Touch ID is a convenience factor for legitimate users, not a mechanism against duress.
- **macOS-side compromise.** If your Mac's Secure Enclave is compromised (which is very hard but not impossible for state-level attackers), the Touch ID enrollment templates are at risk.
- **Loss of the paired Mac.** The Touch ID box paired to a lost Mac provides zero value to whoever finds the Mac — Secure Enclave is bound to that Mac's hardware. But the box paired to that Mac is unusable elsewhere until you re-pair it to a different Mac.
- **Rubber-hose cryptanalysis.** Standard XKCD 538 caveat applies.

## 9.8 Summary posture

For a personal workstation used by a single person or a household of known-trust individuals, this build provides authentication security equivalent to a factory Apple keyboard. Use it as you would use built-in Touch ID on a MacBook — it is not a step down.

For high-security or regulated environments, consult your organization's policy on hardware modifications and homebuilt authentication devices. Some environments will not accept anything that has been physically modified, regardless of preserved cryptographic properties.
