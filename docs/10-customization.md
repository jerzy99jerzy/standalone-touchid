# 10. Customization - Ghost in the Shell aesthetic direction

Everything in this section is taste, not engineering. It is here because a build this small is one of the few where finish is a real part of the outcome, and because deciding the look before you print saves reprinting. None of it affects function, and skipping the whole section costs you nothing.

The 1995 Oshii film and the *Stand Alone Complex* series share a coherent visual language: industrial-grade rather than consumer-grade equipment, minimal typography at high information density, muted palettes with one precise accent, and visible age suggesting field-deployed rather than freshly-unboxed hardware. This build is literally a *standalone* Touch ID, so the joke writes itself.

Four rules for staying in this design register:

1. **Industrial-grade, not consumer-grade** - the device looks like it came from an equipment locker, not a retail store.
2. **Minimal typography, high information density** - serial numbers instead of brand names.
3. **Muted palette + one accent** - charcoal, gunmetal, with cyan or safety orange as the single accent.
4. **Visible age** - light patina suggesting field-deployed hardware.

## 10.1 Four tiers of intervention

Ordered by effort and cost.

### Tier 0 - filament choice alone

Cheapest change, largest visual return, and the only tier that costs no extra time.

Stay in PETG. Dark greys and metallic-pigment blacks are widely available from Spectrum, Fiberlogy, Polymaker and others, but colorway names churn faster than this document updates, so check what your supplier actually stocks rather than hunting a SKU named here. What you want is a dark grey or a black carrying mineral or micro-glitter pigment; both read as anodized metal after a light 320-grit pass.

**Do not substitute ASA or ABS to chase a finish.** They want an enclosure and a hotter bed, the parameters in [section 5](05-print-plan.md) do not apply to them, and the box will warp at the corners without one. A better black is not worth reprinting the C plate for. In PETG, print exactly per section 5 and change nothing but the spool.

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

**Font:** Microgramma D Extended or Eurostile carry the right period feel. Both are commercial Linotype faces, so if you want something libre, Michroma on Google Fonts is the closest near-match worth evaluating. Any of the three debosses cleanly at 0.4 mm without slicer modification.

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

The only tier this guide argues against. It is the one change that puts a soldering iron and a second power source next to a board you cannot replace, in exchange for decoration. It is documented because people will do it anyway.

A single 1206 SMD LED behind a 2 mm semi-transparent window in the enclosure side, with a current-limiting resistor sized for your supply, powered from a separate USB-C breakout at roughly $5. Cyan (#00D9FF) is the accent this documentation uses throughout, a convention adopted here rather than a colour anyone official specified.

**Do not tap the Lightning line for it.** You would be drawing from a power path budgeted for the logic board alone, with no upside and a failure mode that ends in reopening the box.

The effect is one discreet point of light in a dark room. Roughly two hours and a soldering iron. It photographs well, which is most of the honest argument for it.

## 10.2 Aesthetic coherence - building a set

If you plan to add other 3D-printed desk accessories later (YubiKey holder, Apple Watch charging dock, cable management trough) - commit to a unified visual language across them:

- **Same font** - Microgramma / Eurostile / IBM Plex Mono
- **Same palette** - charcoal or gunmetal base, one accent color, same warm-white for typography
- **Same numbering system** - `TID/01`, `KEY/01`, `PWR/01` - all form a coherent rack

Result: a coordinated equipment stack rather than a random pile of black plastic parts.

## 10.3 What reads well on video

If you are filming the thing, Tier 1 and Tier 4 survive a mid-shot: stencil typography holds its contrast and the LED gives the eye somewhere to land.

Tier 2 does not. Weathered metal is excellent in the hand and at close range, and from normal desk distance it reads as a dirty enclosure rather than as intentional patina. Worth knowing before you spend the twenty minutes.
