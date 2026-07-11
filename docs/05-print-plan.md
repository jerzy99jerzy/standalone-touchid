# 5. 3D print plan

## 5.1 The four parts

Four independent parts, printed in two different quality presets. STL files are Calvin's — download from [Printables](https://www.printables.com/model/355924-clickable-touch-id-box-tkl-board-wired). Do not redistribute the STL files; link to source.

| Part | Function |
|------|----------|
| **Box** | Main enclosure body. Houses logic board, Lightning port, button assembly. |
| **Lid** | Top cover, slides in from above. Visible surface of the finished device. |
| **C plate** | Click mechanism plate. Critical tolerance — determines button feel. |
| **Back plate** | Rear closure. Compresses spring plate and secures ribbon cable path. |

## 5.2 Slicer settings per part

Values are calibrated for Calvin's original PETG setup and confirmed by Geerling's build (who had to reprint the C plate at 0.10 mm after a failed 0.12 mm attempt).

| Part | Layer height | Infill | Infill angle | Perimeters | Supports |
|------|-------------|--------|--------------|------------|----------|
| Box | 0.20 mm | 100% | 90° | 3 | No |
| Lid | 0.20 mm | 100% | 90° | 3 | No |
| **C plate** | **0.10 mm** | 100% | 45° | 3 | No |
| Back plate | 0.20 mm | 100% | 45° | 3 | No |

The C plate is flagged in bold because failure to use 0.10 mm layer height produces geometry that either does not click, or leaves the button stuck depressed. This is the one setting you do not compromise on.

## 5.3 PETG material parameters

| Parameter | Value |
|-----------|-------|
| Nozzle temperature | 235–245°C (start at 240°C, calibrate per spool) |
| Bed temperature | 75–85°C (PEI sheet: 80°C; glass: 75°C with PVA stick or Magigoo PETG) |
| Cooling fan | 30–50%, enable from layer 3 |
| Retraction, direct drive | 0.8–1.0 mm @ 35–40 mm/s |
| Retraction, Bowden | 4–5 mm @ 35–40 mm/s |
| First layer height | 0.20 mm (or 0.10 mm for C plate) |
| Outer perimeter speed (C plate only) | Reduce to 30 mm/s for click-mechanism detail |

These are a good starting point. Run a temperature tower on any new spool before printing the C plate — PETG varies more from batch to batch than PLA does.

## 5.4 Bed orientation

- **Box:** Top surface up (the side with the Touch ID button cutout is on top of the print). The most tolerance-critical surfaces are not directly on the bed. Clean top surface and simple print path.
- **Lid:** Flat, visible side up. The angled edges (which slide into the box slot) are oriented sideways and need no supports.
- **C plate:** Flat, fingerprint-detail side up. The central stem is a functional mechanism element, not a support artifact.
- **Back plate:** Flat, either side up.

## 5.5 Post-processing

Three finishing operations after removing the parts from the printer:

1. **Top surface of box and back plate** — light pass with 320-grit sandpaper. Eliminates visible layer lines and produces a matte finish that matches Apple's aesthetic.
2. **Lid edges** — test slide-fit into the box. If too tight, ease with a fine file or 600-grit paper. If loose (lid falls out), do nothing — internal components will hold it in place once installed.
3. **C plate — mandatory test fit with the Touch ID button before final assembly.** Insert the button into the C plate and press. It should give a clean mechanical click. If too stiff or no click, sand the raised central point on the C plate with 600-grit paper, 0.1 mm at a time, testing after each pass. This is the most common failure mode and the most common place to rescue the feel of the button.

## 5.6 Print time

Rough estimate on a mid-tier printer (Prusa MK3S+, Bambu A1, Voron Trident) with default speed profiles:

| Part | Time |
|------|------|
| Box | ~55 min |
| Lid | ~30 min |
| C plate | ~40 min |
| Back plate | ~20 min |
| **Total (sequential)** | **~2.5 hours** |

You can print the box, lid, and back plate in one bed (they fit together on any 200×200 bed). The C plate must print separately because it's on 0.10 mm and the others are on 0.20 mm.
