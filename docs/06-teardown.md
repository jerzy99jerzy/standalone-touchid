# 6. Teardown - Magic Keyboard with Touch ID

The hardest part of this project, and it is not the print. Apple bonds the keyboard together in layers of adhesive; Geerling calls tearing one apart far more daunting than it ought to be. Three things here are easy to destroy for good: the Touch ID flex cable, the battery flex PCB, and the Li-Po cell itself, which does not forgive being bent.

## 6.1 Heating strategy

The adhesive holding the back cover softens to a gum-like state at 50-65°C. Four proven heating methods:

- **Your 3D printer's heated bed (safest).** Set to 60-65°C, place the keyboard face down, wait 5-10 minutes. Adhesive softens evenly across the whole panel.
- **iOpener (microwavable gel pack).** Localized, controlled heat.
- **Heat gun on lowest setting.** What Calvin used. Risk of deforming the keyboard's plastic locally. Keep 10 cm of distance and keep the gun moving.
- **1500W hair dryer.** Slower, safer, works fine.

The heated-bed method is the one Calvin passes along from a commenter on his model page, and it is the least likely to cook anything. Geerling leaned his keyboard against a space heater instead, with the caveat not to melt it. Either works with attention; plastic starts deforming around 80°C, so the risk is inattention rather than method.

## 6.2 Four critical failure points

### Point 1 - the back cover

Start at the edge near the Lightning port - that's where the adhesive is thinnest. Slide a plastic spudger 1-2 mm into the seam, work around the perimeter, freeing adhesive as you go. **Do not insert metal tools deeper than 2 mm** - the battery flex PCB and the battery itself run directly beneath the cover.

Expect to spend 15-20 minutes on this step alone.

### Point 2 - the Li-Po battery

The battery is glued to the lower housing with a thick layer of adhesive. Apple includes a pull-tab strap, but it's weak and often tears prematurely. Proven technique:

1. Load 1-2 ml of 99% isopropyl alcohol into a needle-tip syringe.
2. Inject along the seam between battery and housing.
3. Wait 60 seconds.
4. Gently pry the battery at a constant angle. **Do not bend a single edge upward** - that flexes the cell.

**Warning:** Bending a Li-Po cell can cause internal separator damage, swelling, and thermal runaway. If you see any swelling of the battery, set it aside immediately and stop. This is rare but real. Dispose of the battery through proper e-waste channels - do not throw it in household trash.

### Point 3 - Touch ID ribbon cable to logic board

The flat flex with surface-mount components on it, running from the logic board across to the Touch ID button. Geerling put his odds of tearing it at fifty-fifty while pulling it free, and his did survive. Adhesive holds it firmly to the housing underneath along its whole length.

**Technique:**
1. Do not pull. Lift parallel.
2. Use curved-tip tweezers to un-stick the ribbon corners first.
3. Once the corners are free, lift the entire ribbon slowly and evenly, staying parallel to the underlying surface.
4. If the ribbon resists at some point, add localized heat (hair dryer, 10 seconds) to soften the adhesive under that section.

If this ribbon tears, the keyboard is scrapped. Buy another one.

### Point 4 - Touch ID button keycap

The Touch ID module itself has a plastic keycap on top of the sensor (the square cover with the finger indentation). You must remove this - in the new enclosure, the sensor operates without a keycap, directly under the C plate surface.

The keycap is held by small internal clips. Pry it off gently with the spudger from the edge. Calvin's page shows a photograph of the button as it should look afterwards, and points at [the moment in the SnazzyLabs video where the cap comes off](https://youtu.be/hz9Ek6fxX48?t=374). The cap is glued as well as clipped and breaks easily, so go slower here than the step seems to deserve.

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

The remainder of the keyboard - the plastic housing, the mechanical keys and mechanisms, the battery, the RF antenna, the top and bottom aluminum sheets, all remaining screws - goes to e-waste.

Two of those are worth pausing over, because discarding them is the moment the build becomes one-way. **The battery and the RF antenna together are what made the donor a wireless device.** Once they are out, the finished box is bus-powered and tethered for good: no battery to run on, no antenna to talk over. That is the intended design and Calvin's model is named "wired" accordingly, but it is a decision you make here, with a spudger, rather than later. [Requirements 3.3](03-requirements.md#33-power-and-what-the-build-gives-up) spells out what it costs you.

The battery in particular: dispose properly. Do not throw a used Li-Po in with your regular trash. Most electronics retailers accept them for free recycling.
