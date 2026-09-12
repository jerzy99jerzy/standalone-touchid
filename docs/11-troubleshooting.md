# 11. Troubleshooting decision tree

Common problems and diagnostic paths.

## 11.1 Print issues

### C plate does not click - button sticks depressed

**Diagnosis:** layer height too high, printed at 0.20 or 0.12 mm instead of 0.10 mm, leaving the raised centre point too tall. This is the single most reported failure on this build and Geerling hit it at 0.12 mm.

**Fix:** Reprint the C plate at 0.10 mm layer height. If that still doesn't help, sand the central stem with 600-grit paper, 0.1 mm at a time, testing between passes.

### Lid does not slide into the box, or slides in too loosely

**Diagnosis:** Print tolerance variation, typically from over-extrusion (PETG expands slightly more than PLA between layers).

**Fix:**
- Too tight: file the edges with a fine file or 600-grit paper.
- Too loose: apply a thin strip of electrical tape to the interior edge of the lid to take up the gap. Or reprint with 2-3% smaller flow rate.

### Print warps at the corners

**Diagnosis:** Insufficient bed adhesion or bed temperature too low.

**Fix:** Increase bed temperature by 5°C. Clean bed with isopropyl alcohol. Apply glue stick or Magigoo PETG. Ensure first layer height is correct.

## 11.2 Teardown issues

### Back cover will not come off despite heating

**Diagnosis:** Adhesive did not reach the gum-like temperature.

**Fix:** Increase heating time to 15 minutes on a 65°C heated bed. Alternatively, use a heat gun at 10 cm distance for 30 seconds on each edge before prying.

### Touch ID ribbon cable tore or detached

**Diagnosis:** Too much force during teardown.

**Fix:**
- If detached from the logic board: check the connector for damage; you can often reseat the ribbon with tweezers.
- If the ribbon itself tore: the keyboard is scrapped. Buy another used one.

### Battery pull-tab snapped

**Diagnosis:** Standard Apple pull-tab weakness.

**Fix:** Inject isopropyl alcohol into the seam, wait 90 seconds, pry the battery gently with a spudger at multiple points around the perimeter. Do not concentrate force on one edge.

### Small screws lost during teardown

**Diagnosis:** Screws are M1.2 and extremely easy to lose.

**Fix:** Keep the assembly on a magnetic parts tray or in labeled ziploc bags. When you buy the micro-screw kit ([BOM](04-bom.md)), you get spares.

## 11.3 Pairing issues

### macOS does not detect the device

**Diagnosis:** Charge-only cable, damaged logic board port, or logic board without power.

**Fix:**
1. Try a different USB-C to Lightning cable (known data-capable).
2. Try a different USB-C port on the Mac.
3. Verify the logic board is properly seated in the enclosure.
4. Verify the Lightning port is secure and correctly aligned.

### Touch ID visible in System Settings but enrollment fails

**Diagnosis:** Secure pairing not completed, or re-pairing from a previous Mac requires secure intent gesture.

**Fix:** System Settings → Touch ID & Password → Delete all existing fingerprints, then re-enroll. When prompted, perform the secure intent gesture (double-press power button on Mac).

### First `sudo` authentication clicks but macOS rejects it

**Diagnosis:** Enrollment incomplete or fingerprint enrolled on a different Mac.

**Fix:** Delete all fingerprints in System Settings, enroll from scratch. Enroll the same finger multiple times at slightly different angles for better recognition.

### Touch ID stops working after Mac reboot

**Diagnosis:** Secure Enclave policy - first authentication after boot always requires password.

**Fix:** Enter your password once at the login screen. Subsequent Touch ID prompts will work.

### "Touch ID not available right now"

**Diagnosis:** Policy timeout (48-hour password required) or repeated failed attempts (5-attempt lockout).

**Fix:** Enter your password once to reset. If the message persists, check System Settings → Touch ID & Password for any error state.

## 11.4 When to give up and start over

Some failures are unrecoverable:

- **Torn Touch ID ribbon cable during teardown** - buy another keyboard.
- **Damaged logic board (visible burn marks, bent connectors, cracked components)** - buy another keyboard.
- **Battery swelling or damage during removal** - dispose safely, buy another keyboard.
- **Lost or damaged Touch ID button module** - buy another keyboard.

The keyboard itself is the expensive part; everything else (filament, screws, tools) is cheap. If the electronics are wrecked, cutting your losses and buying a second used keyboard is faster than trying to salvage.

## 11.5 Where to get help

- **GitHub issues on this repo** - documentation gaps, corrections, and build reports
- **[Comments on Calvin's model](https://www.printables.com/model/355924-clickable-touch-id-box-tkl-board-wired/comments)** - the closest thing to an authoritative venue for model-specific questions, and the source of several tips reproduced in this guide
- **[Geerling's blog post](https://www.jeffgeerling.com/blog/2025/why-doesnt-apple-make-standalone-touch-id/)** and its comment thread - discussion of one complete build
- **r/AppleHelp, r/hardware, r/functionalprint on Reddit** - general community support
