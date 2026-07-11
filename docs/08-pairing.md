# 8. Pairing with macOS

Physical assembly is complete. Now the software side.

## 8.1 First connection

1. Connect a USB-C to Lightning cable between your assembled Touch ID box and any USB-C port on your Apple Silicon Mac. Lightning side into the box; USB-C side into the Mac.
2. Wait 5–10 seconds. macOS detects the device automatically. A notification may appear in the Bluetooth menu identifying the device as a Magic Keyboard with Touch ID, even though only the Touch ID subsystem is functional (there are no keys to type on).

## 8.2 Enrollment

3. Open **System Settings → Touch ID & Password**.
4. **If the keyboard was previously paired to another Mac:** macOS prompts for re-pairing and requires a secure intent confirmation — **double-press the power button on your Mac**. The Secure Enclave then rewrites the pairing identity in the box's PKA block.
5. Click **Add Fingerprint**.
6. Enroll: place your finger on the Touch ID button on the box repeatedly at slightly different angles until macOS reports enrollment complete.

## 8.3 Functional test

Open Terminal and run:

```bash
sudo true
```

You should see a Touch ID prompt. Press the button — you'll feel the mechanical click, the prompt dismisses, and `sudo` is authorized without a password.

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
Try a different USB-C port. Try a different USB-C to Lightning cable — not all Lightning cables carry data. Some cheap third-party cables are charge-only.

**"Touch ID not available right now":**
Restart the Mac. Check whether you've hit a policy timeout (48-hour password requirement, or 5-failed-attempt lockout).

## 8.6 Operational note — future Mac migration

If you buy a new Mac later and want to use the same box on it, re-pair using the same procedure. One box is paired to one Mac at a time, but the pairing identity is cyclable without limit. A single Mac can maintain up to 5 simultaneous Touch ID device pairings, so keeping multiple boxes on one Mac is possible.
