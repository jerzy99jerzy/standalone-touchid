# 2. Rejected alternatives

## 2.1 Apple Watch SE

The obvious first thought: instead of cannibalizing a keyboard for around $100, use hardware whose macOS authorization function is already officially supported. Apple Watch (Auto Unlock and Approve with Apple Watch) covers a significant portion of Touch ID's desktop function - `sudo`, unlock Keychain, `pkg` installations, System Settings authorizations - through a double-press of the side button.

### The fundamental problem

Auto Unlock and Approve with Apple Watch require active Wrist Detection. Apple enforces this in watchOS policy: turning Wrist Detection off makes Apple Pay require the passcode and disables Mac unlock entirely.

Therefore, the watch cannot sit on your desk in a 3D-printed cradle as a biometric puck. It must be worn.

### The PPG spoofing workaround

Wrist Detection uses photoplethysmography (green LEDs and IR photodiodes on the back of the watch) combined with the accelerometer. A workaround - placing an absorptive material (dark felt, black silicone) under the PPG sensor combined with a one-time motion to satisfy the accelerometer - keeps the watch in an unlocked state indefinitely.

This works. It also breaks the threat model in an unacceptable way. Anyone with physical access to your desk can authorize `sudo`, install software, use Apple Pay (if enabled), or unlock Keychain items. For a security-conscious workstation, this route is off the table.

### The economics

Second argument against Apple Watch SE: it is not cheaper. Used Apple Watch SE Gen 1 in most markets is $130-180 USD equivalent. Used A2449 Magic Keyboard with Touch ID is $100-140 USD equivalent. The Geerling/Calvin build is cheaper and preserves true biometric authentication with liveness detection.

## 2.2 USB-C fingerprint readers with FIDO2

The second considered alternative is a USB-C fingerprint reader supporting FIDO2/WebAuthn (Kensington VeriMark Guard, Yubico Bio, eikon mini). These devices provide a second factor for compatible web applications and, in some cases, macOS login via passkey. They do not replace Touch ID for system operations - `sudo`, unlock Keychain, and Apple Pay do not use FIDO2.

FIDO2 readers are complementary, not substitutes. They can run in parallel with a Touch ID box for web scenarios, but for native macOS authorization the keyboard cannibalization remains the only real option.

## 2.3 Third-party fingerprint HID devices

Products advertised as "Windows Hello fingerprint readers" that expose HID fingerprint APIs do not integrate with macOS at all. macOS Touch ID API is closed and locked to Apple hardware. There is no way to have a non-Apple sensor talk to the Secure Enclave.

## 2.4 Summary

For a Mac with Apple Silicon, where the goal is a desktop-mounted biometric authenticator with full macOS integration (`sudo`, Keychain, System Settings, Apple Pay) - cannibalizing a Magic Keyboard with Touch ID is the only option. The other paths either don't provide the necessary integration, or provide it at the cost of security posture.
