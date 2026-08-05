# 7. Assembly

Execute the steps in the order given. Some are not reversible without full disassembly. First-time assembly typically takes 45-60 minutes; step 10 (Lightning port) alone often eats 20-30 minutes on the first attempt.

## Sequence

**1. Verify all four parts printed correctly**

All four parts should be off the printer, cleaned of any support material or brim residue, and post-processed per [section 5.5](05-print-plan.md#55-post-processing). Do the C plate test-fit with the Touch ID button before proceeding.

**2. Place Touch ID module in the box**

Insert the Touch ID button module centrally into the box. The fingerprint sensor face is up. The ribbon cable exits toward the side that will accommodate the logic board (Calvin's model has a specific slot for the ribbon).

**3. Fit the C plate over the button**

Verify the ribbon cable routes through the correct slot without strain.

**4. Test the click one more time**

Press the C plate - you should get a clean mechanical click with slight resistance. If too stiff, remove the C plate, sand the central stem lightly with 600-grit paper, and retest. Do not proceed with a stiff click; it will only get worse under assembly compression.

**5. Install the spring plate**

Fit the metal spring plate (original from the keyboard) on top of the C plate. Orientation matters - the longer axis of the spring plate runs along the longer axis of the box. Calvin's Printables page has photos.

**6. Screw the spring plate to the button**

Use the four original micro-screws from the keyboard. Cross-tighten (opposite corners) rather than going around, to avoid uneven compression.

**7. Install the back plate**

**Critical:** The side of the back plate without a screw hole must face the ribbon cable (that is, must face the logic board slot). The back plate is asymmetric; installing it backward makes the next steps impossible.

**8. Screw the back plate on**

Seven M1.2 × 4 mm Phillips screws. Cross-tighten again.

**9. (Optional but recommended) Electrical tape insulation**

Apply a small strip of electrical tape to any metal contact points on the housing that could short against the logic board if a screw ever loosened. Minor ESD/short-circuit insurance.

**10. Install the logic board**

Slide the logic board into its slot in the box. Verify the Touch ID ribbon cable seats without strain. Screw the board down with two M1.2 × 4 mm screws.

**11. Install the Lightning port (hardest step)**

This is the step that eats time. You need to seat the Lightning port into its slot and secure it with two M1.2 × 4 mm screws that thread into two M1.2 nuts on the outside.

**Calvin's technique:** Hold the nut in curved-tip tweezers on the exterior side while threading the screw from the interior side.

**Geerling's technique:** Balance the nut on the tip of the screw, hold the nut with your finger from above, drive the screw from below.

Give yourself 30 minutes for this step on your first build. It gets faster.

**12. Install the lid**

Slide the lid into the box from above. **Critical orientation:** the wider, more angled side of the lid must face the logic board (the longer edge of the box).

**13. (Optional) Rubber feet**

Apply four small adhesive rubber feet to the bottom - two front, two back. Prevents desk slide. Recommended for any surface where the device will move under button pressure.

## Assembly complete

At this point the device is physically finished. Do not connect it to a Mac yet unless you're proceeding directly to pairing - the Lightning port is now the only electrical interface and any fault handled from this point requires reopening the box.

Proceed to [section 8: Pairing](08-pairing.md).
