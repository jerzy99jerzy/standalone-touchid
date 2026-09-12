# 5. 3D print plan

## 5.1 The four parts

Four independent parts, printed in two different quality presets. STL files are Calvin's - download from [Printables](https://www.printables.com/model/355924-clickable-touch-id-box-tkl-board-wired). Do not redistribute the STL files; link to source.

| Part | Function |
|------|----------|
| **Box** | Main enclosure body. Houses logic board, Lightning port, button assembly. |
| **Lid** | Top cover, slides in from above. Visible surface of the finished device. |
| **C plate** | Click mechanism plate. Critical tolerance - determines button feel. |
| **Back plate** | Rear closure. Compresses spring plate and secures ribbon cable path. |

## 5.2 Slicer settings per part

Every value in this table comes from the notes section of Calvin's model page, describing the settings he printed with: a Prusa i3 MK3S+ on a textured PEI sheet, Prusament Jet Black PETG, 100% infill, no supports, box and lid at a 90° fill angle and the C plate and back plate at 45°. In PrusaSlicer terms he used the 0.20 mm QUALITY preset for three parts and the 0.10 mm DETAIL preset for the C plate.

| Part | Layer height | Infill | Infill angle | Supports |
|------|-------------|--------|--------------|----------|
| Box | 0.20 mm | 100% | 90° | No |
| Lid | 0.20 mm | 100% | 90° | No |
| **C plate** | **0.10 mm** | 100% | 45° | No |
| Back plate | 0.20 mm | 100% | 45° | No |

Perimeter count is deliberately absent: Calvin does not state one, so the preset default applies. Three perimeters is a sane choice at 100% infill and nothing here depends on it. The 90° fill angle on the box and lid is cosmetic in origin, chosen for how the top surface looks.

**The C plate at 0.10 mm is the one setting with no room in it.** Calvin puts the instruction in bold on his own page, twice. Print it coarser and the raised centre point comes out too tall, which leaves the button either dead or stuck depressed. Geerling's build corroborates the failure: his slicer default of 0.12 mm produced a plate that sat too high and he reprinted at 0.1 mm. *[He names the part the "Touch ID backing plate" rather than the C plate; Calvin's instruction is unambiguous and is the one to follow.]*

## 5.3 PETG material parameters

| Parameter | Value |
|-----------|-------|
| Nozzle temperature | 235-245°C (start at 240°C, calibrate per spool) |
| Bed temperature | 75-85°C (PEI sheet: 80°C; glass: 75°C with PVA stick or Magigoo PETG) |
| Cooling fan | 30-50%, enable from layer 3 |
| Retraction, direct drive | 0.8-1.0 mm @ 35-40 mm/s |
| Retraction, Bowden | 4-5 mm @ 35-40 mm/s |
| First layer height | 0.20 mm (or 0.10 mm for C plate) |
| Outer perimeter speed (C plate only) | Reduce to 30 mm/s for click-mechanism detail |

Calvin does not publish temperatures, so unlike the table in 5.2 these are conventional PETG values rather than sourced ones. Treat them as a starting point and run a temperature tower on any new spool before committing to the C plate. PETG varies more between batches than PLA does, and the C plate is the part where that variation shows up as a dead button.

## 5.4 Bed orientation

*Orientations below are read off the geometry and Calvin's build photographs rather than stated by him in text.*

- **Box:** Top surface up (the side with the Touch ID button cutout is on top of the print). The most tolerance-critical surfaces are not directly on the bed. Clean top surface and simple print path.
- **Lid:** Flat, visible side up. The angled edges (which slide into the box slot) are oriented sideways and need no supports.
- **C plate:** Flat, fingerprint-detail side up. The central stem is a functional mechanism element, not a support artifact.
- **Back plate:** Flat, either side up.

## 5.5 Post-processing

Three finishing operations after removing the parts from the printer:

1. **Top surface of box and back plate** - light pass with 320-grit sandpaper. Eliminates visible layer lines and produces a matte finish that matches Apple's aesthetic.
2. **Lid edges** - test slide-fit into the box. If too tight, ease with a fine file or 600-grit paper. If loose (lid falls out), do nothing - internal components will hold it in place once installed.
3. **C plate - mandatory test fit with the Touch ID button before final assembly.** This one is Calvin's instruction, not a suggestion: the C plate detail comes out differently on different printers, so put the button into the plate and test the click before you assemble anything. It should give a clean mechanical click. If it is stiff or dead, sand the raised central point with 600-grit paper, 0.1 mm at a time, testing between passes. This is both the most common failure mode and the easiest one to recover from, but only while the box is still open.

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
