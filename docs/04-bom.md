# 4. Bill of Materials

Prices are approximate USD equivalents, spot-checked mid-2026. **They will drift and the used-market ones drift fast.** Treat every figure here as an order of magnitude, re-check before buying, and update the date stamp in this line if you refresh them.

## 4.1 Donor keyboard - most critical BOM line

**The used market is the only route.** Apple's current stock is the USB-C generation (A3118 / A3119); the Lightning A2449 this build needs has been out of Apple's catalogue since the October 2024 refresh, so neither Apple Store nor Apple Refurbished is a path to a donor. Anything advertised as new A2449 is old channel stock, not Apple.

| Source | Condition | Price (USD equiv.) |
|--------|-----------|--------------------|
| eBay, Craigslist, Facebook Marketplace, Reddit r/hardwareswap | Used | $100-140 |
| Remaining retailer channel stock, where it exists | New, old stock | Varies widely, often above used |

For reference, Apple's US list price for the A2449 at launch was $149, and Geerling's writeup describes the build as sacrificing "a $150 keyboard". If a used listing approaches that, the economics of the project stop working.

EU/PL reference, mid-2026: used A2449 on Allegro and OLX ran roughly 400-550 PLN. Verify current asks rather than trusting this line.

**Buying used, verify:**
- Model number **A2449**. The generations carry disjoint numbers, so this is a sufficient test; see the matrix in [requirements 3.1](03-requirements.md)
- **Lightning charging port, not USB-C.** Must agree with the model number. A mismatch means the listing does not describe the hardware, which is disqualifying for an authentication device
- Touch ID works - ask the seller to demonstrate on video
- Includes a data-capable USB-C to Lightning cable, or budget for one. Not just for pairing: the finished box has no battery and runs on bus power, so the cable and one port on your Mac are permanent fixtures. See [requirements 3.3](03-requirements.md#33-power-and-what-the-build-gives-up)
- Inspect for prior opening. Factory adhesive is uniform; a previous entry usually shows along the edges. This is your only pre-purchase tamper check, and [Threat model 9.2](09-threat-model.md#92-supply-chain-and-the-used-donor) explains why it is worth making

## 4.2 Filament

Total consumption for all four parts: 25-40 grams. One spool covers this project and many others.

| Brand | Type | Price/kg (USD equiv.) |
|-------|------|----------------------|
| Prusament PETG Jet Black | Premium, EU-made | ~$32 |
| Spectrum Premium PETG Deep Black | PL-made, excellent quality | ~$22 |
| Fiberlogy Easy PETG Black | Solid mid-range | ~$25 |
| Polymaker PolyLite PETG Black | US/global availability | ~$25 |

**Do not use PLA.** Thermal creep in sunlit conditions and brittleness after months of use both compromise the click mechanism. **Do not use ABS** without a heated enclosure - it will warp at the corners of the box.

## 4.3 Hardware - small screws

Quantities below are Calvin's, from the material list on the model page.

| Item | Quantity | Notes |
|------|----------|-------|
| M1.2 × 4 mm Phillips stainless steel screws | 11 | 7 for the back plate over the button, 2 for the logic board, 2 for the Lightning port mount |
| M1.2 hex or square nuts | 2 | For the Lightning port mount. Calvin also suggests keeping a few slightly longer screws on hand for this step |
| Adhesive rubber feet, ~4 mm | 4 | Optional, prevents desk sliding |
| Electrical tape | trace | Optional, insulates metal that could touch the board if a screw ever backs out |

Best sourced as a mixed micro-screw kit (M1-M2.5 assortment) from Amazon, AliExpress, or your local electronics supplier. Approximately $8-12 for a kit that will last you multiple projects. Micro-screws lose themselves easily; buy the kit.

## 4.4 Tools

If you don't already have these:

| Tool | Price (USD equiv.) | Notes |
|------|--------------------|-------|
| Curved-tip ESD-safe tweezers (0.2 mm tip) | ~$8 | Essential for handling screws and ribbon cable |
| Plastic spudger (iFixit jimmy or equivalent) | ~$5 | You can print this from PETG scraps if you don't want to buy |
| Phillips PH000 screwdriver | ~$6 | Precision size |
| ESD wrist strap | ~$5 | Skip if you have an ESD mat setup already |
| Heat gun or hair dryer | ~$25 (heat gun) / ~$15 (hair dryer) | Needed to soften adhesive |
| Isopropyl alcohol 99% | ~$4 | For loosening battery adhesive |

## 4.5 Total cost summary

| Scenario | Cost (USD equiv.) |
|----------|-------------------|
| Bare minimum - used keyboard, filament and tools on hand | $110-150 |
| Typical build - used keyboard, new filament and small tools | $140-190 |
| Full retail - new keyboard, new filament and tools | $250-290 |

The dominant cost is the donor keyboard. Buy used if at all possible; it is the same hardware and the same working device.

## 4.6 A note on quality

Do not skimp on the tweezers or the screwdriver. Bad tools in this build translate directly to stripped screws, torn ribbon cables, and lost parts. A $6 PH000 screwdriver with a magnetic tip will save you an hour of frustration compared to a $2 no-name from the discount rack.
