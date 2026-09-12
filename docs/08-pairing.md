# 8. Pairing with macOS

Physical assembly is complete. Now the software side.

## 8.1 First connection

1. Connect a USB-C to Lightning cable between your assembled Touch ID box and any USB-C port on your Apple Silicon Mac. Lightning side into the box; USB-C side into the Mac.
2. Wait 5-10 seconds. macOS detects the device automatically and identifies it as a Magic Keyboard with Touch ID, because that is what the logic board reports itself to be.

Be precise about what that means. The keyboard function has not been removed, only its key matrix. *[Inference, not verified on a built unit: the HID keyboard interface should still enumerate, reporting a keyboard that can never produce a keystroke.]* That is cosmetically odd and, if your donor's provenance is uncertain, worth checking rather than shrugging at. [Section 8.6](#86-verifying-what-you-built) covers how.

## 8.2 Enrollment

3. Open **System Settings → Touch ID & Password**.
4. **If the keyboard was previously paired to another Mac:** macOS prompts for re-pairing and requires a secure intent confirmation - **double-press the power button on your Mac**. The Secure Enclave then rewrites the pairing identity in the box's PKA block.
5. Click **Add Fingerprint**.
6. Enroll: place your finger on the Touch ID button on the box repeatedly at slightly different angles until macOS reports enrollment complete.

## 8.3 Functional test

Open Terminal and run:

```bash
sudo true
```

You should see a Touch ID prompt. Press the button - you'll feel the mechanical click, the prompt dismisses, and `sudo` is authorized without a password.

For a second test, try changing a protected setting in System Settings (add a new user account, change firewall settings). macOS should offer Touch ID authorization instead of password entry.

## 8.4 What works after pairing

Once paired, the box provides Touch ID authorization for:

- `sudo` in Terminal, iTerm2, and any shell
- Login screen and wake from sleep (with 48-hour password fallback per Secure Enclave policy)
- Apple Pay in Safari (if enabled in iCloud)
- Unlock Keychain (built-in Keychain; 1Password uses its own stack)
- Authorization of changes in System Settings
- `pkg` installations that require admin
- FileVault (boot requires password; post-boot Touch ID works)

## 8.5 Common issues

**Touch ID button does not respond at all:**
Check ribbon cable seating to logic board. Physically reopen the box, verify the ribbon connector is fully seated. Verify the Lightning port isn't loose.

**Button clicks but macOS doesn't authenticate:**
Enrollment likely incomplete or template mismatch. Delete all fingerprints in System Settings and enroll again.

**macOS does not detect the device:**
Try a different USB-C port. Try a different USB-C to Lightning cable - not all Lightning cables carry data. Some cheap third-party cables are charge-only.

**"Touch ID not available right now":**
Restart the Mac. Check whether you've hit a policy timeout (48-hour password requirement, or 5-failed-attempt lockout).

## 8.6 Verifying what you built

Everything below is read-only. Run it once while the device is known-good and keep the output; it is the baseline you will want the next time something behaves strangely.

```bash
# What enumerates over USB, and under what identity
system_profiler SPUSBDataType | grep -i -B2 -A10 "keyboard"

# Vendor and product identifiers. Apple's vendor ID is 0x05AC
ioreg -p IOUSB -w0 -l | grep -i -E "USB Product Name|idVendor|idProduct"

# Biometric policy state, system domain
bioutil -r -s

# Watch the biometric subsystem during a real authorization,
# then run `sudo true` in a second terminal
log stream --predicate 'subsystem == "com.apple.BiometricKit"' --level info
```

What you are checking:

- The device appears under Apple's vendor ID as a Magic Keyboard with Touch ID. Record the product ID from your own unit rather than copying a number out of someone else's writeup.
- One HID keyboard interface is expected even with no keys attached. An interface you cannot account for is a reason to stop before enrolling a finger, and a reason to re-read [Threat model 9.2](09-threat-model.md#92-supply-chain-and-the-used-donor).
- `sudo true` raises a Touch ID prompt rather than a password prompt, and one physical press completes exactly one authorization.

## 8.7 Operational note - future Mac migration

If you buy a new Mac later and want to use the same box on it, re-pair using the same procedure. One box is paired to one Mac at a time, and the pairing identity is cyclable without limit. *[The figure of five simultaneous keyboard pairings per Mac circulates widely but this guide has not traced it to an Apple source; treat it as unverified rather than as a limit to design around.]*
