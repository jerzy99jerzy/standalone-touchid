# 10. Customization - Ghost in the Shell aesthetic direction

The 1995 Oshii film and the *Stand Alone Complex* series established a coherent visual language: industrial-grade rather than consumer-grade equipment, minimal typography with high information density, muted palettes with one precise accent color, and visible age suggesting field-deployed rather than freshly-unboxed hardware. This build is literally a *standalone* Touch ID; the aesthetic has built-in thematic justification.

Four rules for staying in this design register:

1. **Industrial-grade, not consumer-grade** - the device looks like it came from an equipment locker, not a retail store.
2. **Minimal typography, high information density** - serial numbers instead of brand names.
3. **Muted palette + one accent** - charcoal, gunmetal, occasional cyan (Motoko's signature) or safety orange.
4. **Visible age** - light patina suggesting field-deployed hardware.

## 10.1 Four tiers of intervention

Ordered by effort and cost.

### Tier 0 - filament choice alone

Cheapest change with the largest visual impact.

- **Polymaker PolyLite ASA Galaxy Black** - deep black with micro-glitter mineral pigment, mimics anodized metal
- **Spectrum Premium PETG "Gunmetal Grey"** - approximates brushed steel after light 320-grit sanding
- **Fiberlogy "Tungsten Grey" PETG** - graphite-loaded, actually metallic to touch and under light

Zero extra work. Print exactly per [section 5](05-print-plan.md) with substituted filament.

### Tier 1 - slicer emboss

Calvin's model is available for editing in Tinkercad. Add a 0.4-0.6 mm deboss on the lid's top surface with this typographic layout - keep GitS labeling proportions (dense, asymmetric, not centered):

```
TID/01
公安9課
SER 26·0617
```

Line 1: model number (device tag for your home lab, useful if you build more than one accessory).
Line 2: kanji "Kōan Kyū-ka" - Public Security Section 9, direct anime reference.
Line 3: faux serial number with build date in YY·MMDD format.

**Font:** Microgramma D Extended, or free equivalent Eurostile. Prints cleanly at 0.4 mm deboss without slicer modification.

### Tier 2 - chemical post-processing

Where the device gains its field-deployed look. After printing in black PETG:

1. Full-surface 320-grit sanding of the top face.
2. Thin layer of Vallejo Model Air "Aluminum" or "Gunmetal" applied with dry-brush technique (brush barely loaded with paint, drags across the surface, hitting only edges and raised features).
3. Fill the Tier 1 deboss with Vallejo Model Color "Off-White" thinned with retarder medium - paint flows into recesses, clean typography emerges on the dark background.

Time: 20 minutes. Cost: ~$8 in paints, which cover 50 such projects.

### Tier 3 - hardware accent

Cable-level customization.

- Replace the stock white Apple cable with a black nylon-braided USB-C to Lightning cable (Anker MFi, ~$18) or a custom paracord-sleeved cable (custom cable makers on Etsy, ~$12).
- 3D-printed strain relief in the shape of an octagonal panel-mount connector between the enclosure and cable - adds visual mass and protects the port.
- Small brushed aluminum ID plate (15 × 8 mm) laser-engraved with model and serial, glued into a recess on the enclosure side.

### Tier 4 - LED status accent (advanced)

Warned against in the [build guide](../README.md) but included here for completeness.

A single 1206 SMD LED in cyan (#00D9FF - the signature Major Kusanagi color) behind a 2 mm semi-transparent window in the enclosure side, powered from a separate USB-C breakout (~$5 from Adafruit).

**Do not tap the Lightning line.** That will break power to the logic board.

Effect: one discreet point of light visible in low-light conditions, suggests the device is "live". Integration time ~2 hours, requires soldering, but delivers a finishing touch that reads well on video.

## 10.2 Aesthetic coherence - building a set

If you plan to add other 3D-printed desk accessories later (YubiKey holder, Apple Watch charging dock, cable management trough) - commit to a unified visual language across them:

- **Same font** - Microgramma / Eurostile / IBM Plex Mono
- **Same palette** - charcoal or gunmetal base, one accent color, same warm-white for typography
- **Same numbering system** - `TID/01`, `KEY/01`, `PWR/01` - all form a coherent rack

Result: a coordinated equipment stack rather than a random pile of black plastic parts.

## 10.3 What reads well on video

For content creators - Tier 1 (Section 9 stencil) and Tier 4 (cyan LED) read cleanest on a mid-shot camera. Stencil typography has good contrast ratio; the LED is a visible attention point.

Tier 2 (weathered metal) looks phenomenal at close range but may read as "dirty enclosure" from a normal desk distance rather than intentional patina.
