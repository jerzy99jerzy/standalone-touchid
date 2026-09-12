# 2. Rejected alternatives

## 2.1 Apple Watch SE

The obvious first thought: instead of cannibalizing a keyboard for around $100, use hardware whose macOS authorization function is already officially supported. Apple Watch (Auto Unlock and Approve with Apple Watch) covers a significant portion of Touch ID's desktop function - `sudo`, unlock Keychain, `pkg` installations, System Settings authorizations - through a double-press of the side button.

### The fundamental problem

Auto Unlock and Approve with Apple Watch require active Wrist Detection. Apple enforces this in watchOS policy: turning Wrist Detection off makes Apple Pay require the passcode and disables Mac unlock entirely.

Therefore, the watch cannot sit on your desk in a 3D-printed cradle as a biometric puck. It must be worn.

### Why the obvious workaround is not one

Wrist Detection combines photoplethysmography, the green LEDs and IR photodiodes on the back of the watch, with the accelerometer. Both signals can be satisfied by a watch sitting on a desk rather than on a wrist, and people do this.

It works, and it is still the wrong answer. Defeating Wrist Detection converts the watch from something that authenticates a present, living wearer into a token that authorizes anyone who reaches your desk: `sudo`, software installs, Apple Pay if enabled, Keychain items. That is not a smaller version of Touch ID, it is the removal of the only thing making the watch an authenticator. The mechanics of the bypass are left out here deliberately; the conclusion is what matters and the conclusion is that this route is off the table.

### The economics

The second argument is that it is not even cheaper. Spot-checked mid-2026, a used Apple Watch SE first generation ran $130-180 USD equivalent against $100-140 for a used A2449. *[Both figures are used-market prices and will drift; the point is the ordering, not the numbers.]* The keyboard route came out cheaper and kept capacitive subdermal sensing, which the watch does not offer at all.

## 2.2 USB-C fingerprint readers with FIDO2

The second considered alternative is a USB-C fingerprint reader supporting FIDO2/WebAuthn (Kensington VeriMark Guard, Yubico Bio, eikon mini). These devices provide a second factor for compatible web applications and, in some cases, macOS login via passkey. They do not replace Touch ID for system operations - `sudo`, unlock Keychain, and Apple Pay do not use FIDO2.

FIDO2 readers are complementary, not substitutes. They can run in parallel with a Touch ID box for web scenarios, but for native macOS authorization the keyboard cannibalization remains the only real option.

## 2.3 Third-party fingerprint HID devices

Products advertised as "Windows Hello fingerprint readers" that expose HID fingerprint APIs do not integrate with macOS at all. macOS Touch ID API is closed and locked to Apple hardware. There is no way to have a non-Apple sensor talk to the Secure Enclave.

## 2.4 Summary

For a Mac with Apple Silicon, where the goal is a desktop-mounted biometric authenticator with full macOS integration (`sudo`, Keychain, System Settings, Apple Pay) - cannibalizing a Magic Keyboard with Touch ID is the only option. The other paths either don't provide the necessary integration, or provide it at the cost of security posture.
