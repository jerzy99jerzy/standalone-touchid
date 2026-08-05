# 4. Bill of Materials

Prices below are approximate USD equivalents from mid-2026 markets. EU and PL prices are noted where the author verified them; other markets should adjust accordingly.

## 4.1 Donor keyboard - most critical BOM line

| Source | Condition | Price (USD equiv.) |
|--------|-----------|--------------------|
| eBay, Craigslist, Facebook Marketplace, Reddit r/hardwareswap | Used | $100-140 |
| Apple Refurbished | Refurbished | ~$150 |
| Apple Store | New | $199 |

EU/PL reference: used A2449 on Allegro/OLX runs 400-550 PLN; Apple Store PL sells new for 749 PLN.

**Buying used, verify:**
- Model number **A2449** (TKL, not A2520 numpad version)
- **Lightning charging port, not USB-C** (Apple switched this generation to USB-C on 2024-10-28; the Calvin enclosure targets the Lightning generation, see [requirements 3.1](03-requirements.md))
- Touch ID works - ask the seller to demonstrate on video
- Includes USB-C to Lightning cable - you need one for pairing tests
- Visually inspect for prior opening - factory adhesive has a characteristic uniform appearance; prior openings are usually visible on the edges

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

| Item | Quantity | Notes |
|------|----------|-------|
| M1.2 × 4 mm Phillips stainless steel screws | 11 | 7 for back plate, 2 for logic board, 2 for Lightning port mount |
| M1.2 hex or square nuts | 2 | For Lightning port mount |
| Adhesive rubber feet, ~4 mm | 4 | Optional, prevents desk sliding |

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
