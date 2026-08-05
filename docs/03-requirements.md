# 3. Requirements and constraints

## 3.1 Donor hardware - critical compatibility

**The Calvin enclosure model is designed only for the TKL (tenkeyless) version of Magic Keyboard with Touch ID.** This is the smaller version without the numeric keypad on the right side. The full-size variant with numpad has a significantly larger logic board that will not physically fit.

- **Correct donor:** Model **A2449**, TKL layout, Lightning-charging generation
- **Incorrect donor:** Model A2520 (Magic Keyboard with Touch ID and Numeric Keypad) will not fit
- **Verification:** Model number is on the underside of the keyboard, in small print

When purchasing used, request confirmation of the model number before payment.

### Critical: Lightning generation vs USB-C generation

On October 28, 2024, Apple revised the Magic Keyboard line to charge over USB-C instead of Lightning. This matters for the build. Calvin's enclosure was designed around the Lightning-era logic board and its Lightning port. The internal board layout and the charge/data port on the newer USB-C generation differ, and there is no guarantee the USB-C generation board fits the enclosure or that the port cutout aligns.

Marketplace listings are muddy on this point. Some sellers list a "2024" A2449 with a USB-C cable in the box (the cable being USB-C to Lightning does not make the keyboard a USB-C keyboard). Others list the genuinely new USB-C generation. Before buying:

- Confirm the keyboard's own charging port is **Lightning**, not USB-C. Ask the seller for a photo of the port on the back edge of the keyboard.
- A Lightning port is the small flat oval Apple connector. A USB-C port is the rounded-rectangle symmetric connector.
- If in doubt, favor a unit clearly described as the pre-October-2024 generation.

This guide and the Calvin enclosure target the **Lightning** generation. If someone adapts the enclosure for the USB-C generation, that is a separate model and not covered here.

## 3.2 Target Mac - Apple Silicon required

Magic Keyboard with Touch ID is officially supported only on Macs with Apple Silicon (M1 and later). Intel Macs with the T2 chip contain a Secure Enclave and theoretically support some functions, but Apple does not support Touch ID via Magic Keyboard on this configuration and the pairing procedure is not guaranteed to succeed.

If your Mac is Intel-based, this project is not for you.

## 3.3 Re-pairing when buying used

A used keyboard was most likely paired to the previous owner's Mac. This is not a problem. The Secure Enclave on your Mac will initiate a user-initiated re-pairing through System Settings, overwriting the identity stored in the keyboard's PKA block.

Re-pairing requires only the secure intent gesture (double-press of the power button on your Mac when macOS prompts). There is no "buyer lock" or Activation Lock equivalent for these keyboards. Pairing identity is cyclable without limit.

## 3.4 3D printer environment

- **Nozzle:** 0.4 mm standard.
- **Heated bed:** Required. PETG needs 75-85°C bed temperature.
- **Minimum layer height:** 0.10 mm - the critical C plate part must print at this resolution. Most consumer FDM printers meet this easily.
- **Enclosure:** Not required for PETG. Nice to have, not necessary.
- **Not recommended:** Resin (SLA) printing. Standard resins are too brittle for a part that will be pressed thousands of times.

Verified working printer families: Prusa MK3S/MK4, Bambu A1/P1/X1, Voron 2.4, Creality K1, Sovol SV06+, Ender 3 V3 SE. Anything comparable will work.

## 3.5 Assumed skills

- Basic FDM printing - you can slice a model, configure a filament profile, and diagnose common print failures.
- Basic electronics repair - you can disassemble a small adhesive-bonded consumer electronics device without destroying it. You have a plastic spudger and use it correctly. You understand ESD.
- No soldering required.

## 3.6 Time budget

- **Print time (all four parts, sequential):** 2.5-4 hours
- **Keyboard teardown:** 60-90 minutes on first attempt
- **Mechanical assembly:** 45-60 minutes
- **macOS pairing:** 5 minutes
- **Total on build day:** 4-6 hours (print can run in parallel with teardown)

Budget the full afternoon. Do not try to compress this - the teardown step has irreversible failure points and needs your full attention.

## 3.7 What you cannot skip

Three things you must have before starting the actual build:

1. **The correct A2449 TKL keyboard in hand** - verify model number before opening.
2. **A USB-C to Lightning cable** - required for pairing and normal operation. Not all Lightning cables are data-capable; you need a certified data cable.
3. **All four parts already printed and test-fitted** - do not open the keyboard until the C plate has been verified for click feel. If the print doesn't work, you want to iterate on the print without an open keyboard sitting on your workbench.
