# 6. Teardown — Magic Keyboard with Touch ID

The hardest part of this project. Not the print. Apple adhesive-bonds the keyboard in multiple layers. Geerling described this phase as more stressful than the actual build — three specific elements are easy to permanently destroy: the Touch ID ribbon cable, the battery flex PCB, and the Li-Po cell itself (bending it means pyrotechnics).

## 6.1 Heating strategy

The adhesive holding the back cover softens to a gum-like state at 50–65°C. Four proven heating methods:

- **Your 3D printer's heated bed (safest).** Set to 60–65°C, place the keyboard face down, wait 5–10 minutes. Adhesive softens evenly across the whole panel.
- **iOpener (microwavable gel pack).** Localized, controlled heat.
- **Heat gun on lowest setting.** Risk of localized ABS deformation on the keyboard plastic. Keep 10 cm distance, keep the gun moving continuously.
- **1500W hair dryer.** Slower, safer, works fine.

Geerling propped his keyboard against a convection radiator. That works, but requires close monitoring — plastic starts deforming around 80°C.

## 6.2 Four critical failure points

### Point 1 — the back cover

Start at the edge near the Lightning port — that's where the adhesive is thinnest. Slide a plastic spudger 1–2 mm into the seam, work around the perimeter, freeing adhesive as you go. **Do not insert metal tools deeper than 2 mm** — the battery flex PCB and the battery itself run directly beneath the cover.

Expect to spend 15–20 minutes on this step alone.

### Point 2 — the Li-Po battery

The battery is glued to the lower housing with a thick layer of adhesive. Apple includes a pull-tab strap, but it's weak and often tears prematurely. Proven technique:

1. Load 1–2 ml of 99% isopropyl alcohol into a needle-tip syringe.
2. Inject along the seam between battery and housing.
3. Wait 60 seconds.
4. Gently pry the battery at a constant angle. **Do not bend a single edge upward** — that flexes the cell.

**Warning:** Bending a Li-Po cell can cause internal separator damage, swelling, and thermal runaway. If you see any swelling of the battery, set it aside immediately and stop. This is rare but real. Dispose of the battery through proper e-waste channels — do not throw it in household trash.

### Point 3 — Touch ID ribbon cable to logic board

This is the ribbon Geerling described as 50/50 whether it would tear during his pull. It runs from the Touch ID button assembly under the keyboard chassis, connecting to the logic board. Adhesive holds it firmly to the underlying housing.

**Technique:**
1. Do not pull. Lift parallel.
2. Use curved-tip tweezers to un-stick the ribbon corners first.
3. Once the corners are free, lift the entire ribbon slowly and evenly, staying parallel to the underlying surface.
4. If the ribbon resists at some point, add localized heat (hair dryer, 10 seconds) to soften the adhesive under that section.

If this ribbon tears, the keyboard is scrapped. Buy another one.

### Point 4 — Touch ID button keycap

The Touch ID module itself has a plastic keycap on top of the sensor (the square cover with the finger indentation). You must remove this — in the new enclosure, the sensor operates without a keycap, directly under the C plate surface.

The keycap is held by small internal clips. Pry it off gently with the spudger from the edge. Calvin's Printables page shows a photograph of what the button should look like after keycap removal.

## 6.3 Parts to extract

After full teardown, retain the following for reassembly in the new enclosure:

| Component | Notes |
|-----------|-------|
| Circuit board (logic board) | The green PCB with all the ICs |
| Lightning port assembly | The port plus its metal mounting bracket |
| Touch ID button module + ribbon cable | Keycap already removed |
| Spring plate | Metal spring under the Touch ID button in the original keyboard |
| 4× original micro-screws | The ones that hold the spring plate to the button |

## 6.4 What to discard

The remainder of the keyboard — the plastic housing, the mechanical keys and mechanisms, the battery, the RF antenna, the top and bottom aluminum sheets, all remaining screws — goes to e-waste.

The battery in particular: dispose properly. Do not throw a used Li-Po in with your regular trash. Most electronics retailers accept them for free recycling.
