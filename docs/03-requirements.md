# 3. Requirements and constraints

## 3.1 Donor hardware - critical compatibility

**The Calvin enclosure model is designed only for the TKL (tenkeyless) version of Magic Keyboard with Touch ID.** This is the smaller version without the numeric keypad on the right side. The full-size variant with numpad has a significantly larger logic board that will not physically fit.

- **Correct donor:** Model **A2449**, TKL layout, Lightning-charging generation
- **Incorrect donor:** anything else in the family, per the matrix below
- **Verification:** the model number is printed in small type on the underside of the keyboard

| Generation | Touch ID, TKL | Touch ID with numeric keypad |
|---|---|---|
| Lightning, 2021 | **A2449 - the donor this build requires** | A2520 |
| USB-C, late 2024 | A3118 | A3119 |

The four model numbers are disjoint, which makes the model number a sufficient test on its own. A2520 and A3119 carry a larger logic board; A3118 is the right size but the wrong generation.

"Will not fit" here means Calvin's box specifically, and that is worth separating from a claim about the hardware. The Snazzy Labs model this one remixes ships in three variants, including one drawn around the 109-key board, so a numpad donor is a wrong donor for this enclosure rather than a useless one. Pick the enclosure first, then buy to match it.

When purchasing used, request confirmation of the model number before payment.

### Critical: Lightning generation vs USB-C generation

Apple moved the Magic Keyboard line to USB-C charging in late October 2024, alongside the M4 iMac. *[Sources put the announcement on 28 October and availability a couple of days later; treat "late October 2024" as the reliable form.]* Calvin's enclosure was designed around the Lightning-era logic board and its Lightning port. Board layout and the charge port both changed, so there is no reason to expect a USB-C board to fit the box or the port cutout to line up.

Marketplace listings are muddy. Sellers describe a "2024" A2449 because the box shipped with a USB-C to Lightning cable, which says nothing about the keyboard's own port. Two independent checks:

- **Model number**, from the underside. A2449 is Lightning, full stop. There is no USB-C A2449.
- **The port itself.** Ask for a photo of the back edge. Lightning is the small flat oval; USB-C is the symmetric rounded rectangle.

These two must agree. A listing claiming A2449 while showing a USB-C port is not a careless seller, it is a device whose label does not match its hardware, and for something whose job is authorization that is a reason to buy elsewhere. See [Threat model 9.2](09-threat-model.md#92-supply-chain-and-the-used-donor) for why provenance is the one risk class this build genuinely adds.

This guide and Calvin's enclosure target the **Lightning** generation. Adapting the box to the USB-C generation would be a different model and is out of scope here.

## 3.2 Target Mac - Apple Silicon required

Magic Keyboard with Touch ID is officially supported only on Macs with Apple Silicon (M1 and later). Intel Macs with the T2 chip contain a Secure Enclave and theoretically support some functions, but Apple does not support Touch ID via Magic Keyboard on this configuration and the pairing procedure is not guaranteed to succeed.

If your Mac is Intel-based, this project is not for you.

## 3.3 Power, and what the build gives up

This is the constraint most likely to surprise someone who knows the donor as a Bluetooth keyboard, and it is a constraint on your desk rather than on the build.

**The finished device is bus-powered and permanently tethered.** The Li-Po cell comes out during teardown and is discarded, so there is no internal power source. Everything the box does, it does on power drawn from the host over the Lightning port. Unplug the cable and it is an inert lump of PETG.

**There is no wireless mode, and it cannot be added back.** The RF antenna is discarded alongside the battery in [teardown 6.4](06-teardown.md#64-what-to-discard). This is not a configuration you have switched off; the hardware is gone. Calvin's model is named "wired" for a reason.

That choice is made when you pick an enclosure, not later. The Snazzy Labs model includes a wireless variant sized to keep the cell, which is why it is the larger of the two. *[This guide has not tested that variant and makes no claim about whether Bluetooth still works in it.]* If a battery matters to you, decide before you buy a donor, because after teardown the decision is behind you.

**A data-capable USB-C to Lightning cable occupies one port on your Mac, permanently.** Not a charge-only cable. Budget the port as a standing cost of the build rather than as something you plug in when needed.

*[Inference. The board is assumed to run on bus power alone with no cell present. No source states this outright, but three independent builds (SnazzyLabs, Calvin, Geerling) are all battery-less and wired, which is about as good as empirical evidence gets short of a datasheet. Nobody has published a current draw figure, so this guide does not quote one.]*

### Open question: hubs and docks

Every documented build connects the box directly to a port on the Mac. Whether it enumerates reliably behind a USB-C hub, a dock, or a monitor's downstream ports is **not known**, and this guide will not guess in either direction.

The cryptography is indifferent to topology: attestation and the AES-GCM session run end to end between the PKA block and the Secure Enclave, and an intermediate hub is no more part of that trust chain than a cable is. Enumeration and power delivery are a different matter and are where cheap hubs fail.

If you run a docked laptop, this is the question that decides whether the project fits your desk, and it is unanswered. If you build one, the [build report template](../.github/ISSUE_TEMPLATE/build-report.yml) asks for your topology; that is how this section eventually gets an answer.

## 3.4 Re-pairing when buying used

A used keyboard was most likely paired to the previous owner's Mac. This is not a problem. The Secure Enclave on your Mac will initiate a user-initiated re-pairing through System Settings, overwriting the identity stored in the keyboard's PKA block.

Re-pairing requires only the secure intent gesture (double-press of the power button on your Mac when macOS prompts). There is no "buyer lock" or Activation Lock equivalent for these keyboards. Pairing identity is cyclable without limit.

## 3.5 3D printer environment

- **Nozzle:** 0.4 mm standard.
- **Heated bed:** Required. PETG needs 75-85°C bed temperature.
- **Minimum layer height:** 0.10 mm - the critical C plate part must print at this resolution. Most consumer FDM printers meet this easily.
- **Enclosure:** Not required for PETG. Nice to have, not necessary.
- **Not recommended:** Resin (SLA) printing. Standard resins are too brittle for a part that will be pressed thousands of times.

Verified working printer families: Prusa MK3S/MK4, Bambu A1/P1/X1, Voron 2.4, Creality K1, Sovol SV06+, Ender 3 V3 SE. Anything comparable will work.

## 3.6 Assumed skills

- Basic FDM printing - you can slice a model, configure a filament profile, and diagnose common print failures.
- Basic electronics repair - you can disassemble a small adhesive-bonded consumer electronics device without destroying it. You have a plastic spudger and use it correctly. You understand ESD.
- No soldering required.

## 3.7 Time budget

- **Print time (all four parts, sequential):** 2.5-4 hours
- **Keyboard teardown:** 60-90 minutes on first attempt
- **Mechanical assembly:** 45-60 minutes
- **macOS pairing:** 5 minutes
- **Total on build day:** 4-6 hours (print can run in parallel with teardown)

Budget the full afternoon. Do not try to compress this - the teardown step has irreversible failure points and needs your full attention.

## 3.8 What you cannot skip

Three things you must have before starting the actual build:

1. **The correct A2449 TKL keyboard in hand** - verify model number before opening.
2. **A USB-C to Lightning cable** - required for pairing and normal operation. Not all Lightning cables are data-capable; you need a certified data cable.
3. **All four parts already printed and test-fitted** - do not open the keyboard until the C plate has been verified for click feel. If the print doesn't work, you want to iterate on the print without an open keyboard sitting on your workbench.
