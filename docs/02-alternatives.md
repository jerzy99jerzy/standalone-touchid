# 2. Alternatives

Three paths considered and rejected, and one that is not rejected at all.

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

## 2.4 Buying one already built

This is the alternative that is not rejected, and for most people it is the right answer.

A small market exists for finished modules. Search Etsy or eBay for "standalone Touch ID module" and you will find several sellers, alongside a handful of storefronts that advertise plug-and-play Touch ID for any keyboard. MacSources reviewed one bought from an eBay seller in April 2026. *[Spot-checked September 2026. Storefronts in this category are one-person operations and come and go, so venue names will outlast specific links.]*

They are selling the same thing this guide describes. The hardware path to the Secure Enclave is closed, so every one of these modules starts life as a Magic Keyboard that somebody took apart. The unavoidable part of the project is the cannibalization; the part that is optional is whether you do it. If you want the object rather than the exercise, buy one and skip sections 5 through 7 entirely.

### What buying costs you, in security terms

One thing, and it is the thing this repository is about.

[Threat model 9.2](09-threat-model.md#92-supply-chain-and-the-used-donor) argues that donor provenance is the single risk class this build adds, because attestation authenticates the biometric channel and not the donor's retained HID interface. That argument applies to a purchased module in full, and then some: you are receiving a used authenticator that a stranger opened, reassembled, and closed again, and you never saw inside it.

The awkward part of doing the teardown yourself is also its one security advantage. You handle every component, you see the whole board, and you can photograph the internals against published teardown references before you ever pair it. Buy the finished article and you trade that inspection for an afternoon of your time. Whether that is a good trade depends entirely on who you are and who might care, and for most buyers it plainly is.

What you do not lose is authenticity of the silicon. A seller cannot substitute a non-Apple sensor or a cloned PKA block, because the module would simply fail to pair. Attestation closes that question for a purchased module exactly as it does for one you built.

### Practical notes for buyers

- **Ask whether the module has a battery.** Wired builds omit the cell and must stay plugged in; wireless builds retain it. Listings are not always explicit. [Requirements 3.3](03-requirements.md#33-power-and-what-the-build-gives-up) covers what the wired architecture means day to day.
- **Ask which keyboard generation the board came from**, for the same reasons a self-builder checks the model number.
- **Expect no support.** Apple supports none of this, and neither, realistically, does a one-person shop.
- **Several sellers appear to be selling community designs.** *[Inference from wording: at least one storefront's product description closely tracks the Snazzy Labs model page, down to its three-variant structure.]* Whether that is permitted turns on the licence each designer chose, which is worth a thought if attribution matters to you.

## 2.5 Summary

For an Apple Silicon Mac, where the goal is a desk-mounted biometric authenticator with full macOS integration (`sudo`, Keychain, System Settings, Apple Pay), a cannibalized Magic Keyboard with Touch ID is the only thing that works. Every other sensor is locked out of the Secure Enclave by design.

That is a statement about hardware, not about labour. Somebody has to take a keyboard apart, but it does not have to be you, and [2.4](#24-buying-one-already-built) is a legitimate route. The rest of this guide is written for the case where it is.
