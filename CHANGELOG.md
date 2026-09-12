# Changelog

All notable changes to this documentation are recorded here. This project versions the documentation, not a software release; "version" means a coherent state of the build guide.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) loosely, adapted for a documentation repo.

## [1.3.0] - 2026-09

### Fixed
- **Attribution lineage in `CREDITS.md` was backwards.** The repository stated that Calvin remixed GLOUPY's box and that GLOUPY derived from SnazzyLabs. The model origin data on Calvin's Printables page records the opposite relationship: Calvin's box is a remix of SnazzyLabs' model 320000, which supplied the main design, with the click mechanism separately credited as inspired by GLOUPY's model 349777. Corrected, and Calvin's own list of changes over SnazzyLabs added.
- **`docs/04-bom.md` listed purchase routes that no longer exist.** Apple Store and Apple Refurbished rows offered the A2449 at $199 and ~$150. Apple's current stock is the USB-C generation, so neither is a path to the Lightning donor this build requires; the $199 figure also did not match the A2449's $149 launch list. Both rows removed, the used market named as the only route, and remaining figures date-stamped as drifting.
- **`docs/06-teardown.md` misattributed two details to Geerling.** He leaned the keyboard against a space heater, not a convection radiator, and he did not describe teardown as more stressful than assembly; he called the final assembly step the most annoying part of his build. Both corrected, and the heated-bed method re-credited to the commenter on Calvin's page who suggested it.
- **`docs/05-print-plan.md` presented an unsourced perimeter count inside a sourced table.** Calvin specifies layer height, infill, fill angle and supports, and says nothing about perimeters. The column is removed and the omission explained rather than silently filled.
- **`docs/10-customization.md` contradicted the BOM.** Tier 0 recommended an ASA filament while instructing the reader to print per section 5, which carries PETG parameters, and while section 4 warns against ABS-family materials without an enclosure. Tier 0 is now PETG-only with the reason given.
- **`docs/10-customization.md` referenced a warning the README does not contain.** Tier 4 claimed to be "warned against in the build guide"; no such warning existed. The argument against Tier 4 is now made in place, and a current-limiting resistor added to the description.
- **`.gitignore`** contained the one em-dash that survived the v1.1 sweep, which covered Markdown only.

### Changed
- **`docs/09-threat-model.md` rewritten.** Section 9.2 previously concluded that supply-chain attack is "blocked at the pairing protocol level"; attestation covers the biometric channel and not the retained HID interface, so the section now separates what attestation does and does not reach and treats donor provenance as the one risk class this build genuinely adds. Section 9.3 claimed the sensor "does not respond to" mould and photograph attacks; capacitive sensors including Touch ID have documented laboratory defeats and Apple publishes no PAD rating, so the claim is scoped to opportunistic attacks. Section 9.5 claimed fingerprints are "absolutely protected", which contradicted the coercion entry in 9.7 of the same document. Section 9.1 now says no publicly documented practical attack rather than none.
- **Requirements and BOM now discriminate donors by model number.** The Lightning and USB-C generations carry disjoint numbers (A2449 / A2520 against A3118 / A3119), which makes the model number a sufficient test and makes a model-and-port mismatch a provenance signal rather than seller sloppiness. The refresh date is given as late October 2024, since sources place the announcement and the availability a couple of days apart.
- **`docs/08-pairing.md` corrected its account of what the puck is.** Section 8.1 said only the Touch ID subsystem is functional; the key matrix is discarded but the keyboard function is not removed, and the HID interface is expected to persist. Stated as inference, since no built unit has been checked.
- **Untraced figures are now labeled.** The claim that a Mac maintains up to five simultaneous keyboard pairings appears in two documents and could not be traced to an Apple source; it is marked untraced in both rather than repeated or deleted.
- **`docs/02-alternatives.md` no longer documents the Wrist Detection bypass procedurally.** The conclusion is what the section needed; the recipe was not.
- **Prose pass across all twelve documents.** Sourced statements separated from inferred ones in the text rather than only in principle, absolute constructions softened where the evidence does not support them, and attributions made specific enough to check.

### Added
- **README restructured around the security argument.** A trust boundary table showing which layers are untouched Apple silicon and which single layer the build changes, a per-attack-class comparison against a factory keyboard, a section on the used-donor risk, and an epistemic-discipline statement.
- **`docs/08-pairing.md` section 8.6, verification.** Read-only `system_profiler`, `ioreg`, `bioutil -r -s` and `log stream` checks for confirming what enumerated before enrolling a fingerprint, with a note to keep the output as a known-good baseline. The repository previously asserted that the security posture survived and gave the reader no way to check it.
- **`docs-site/README.md`** recording how the rendered pages were produced, what the bundle contains, and why the Markdown sources remain authoritative.
- **`SECURITY.md`, `CONTRIBUTING.md`, and a build-report issue template.**
- **`.github/workflows/docs-check.yml`**: weekly external link check plus a style gate covering the whole tree rather than Markdown alone.

### Known gaps
- No unit has been built from this guide. The renders are of a reference model, not of hardware, and the inference about the HID interface stays unverified until that changes.
- The license on Calvin's model page is referenced rather than asserted; confirm it on the page before remixing.

## [1.2.0] - 2026-09

### Added
- `docs-site/`: a rendered face of the same documentation, as self-contained HTML with no build step. `index.html` is the interactive build guide (all twelve sections on one page, with print, teardown, assembly and pairing checklists that persist locally), `deck.html` a fifteen-slide project deck with speaker notes, `print.html` the paginated guide for paper, and `enclosure.html` a 3D reference model of the enclosure.
- `assets/renders/`: six stills of the reference enclosure model at 2400x1350, two of them dimensioned, plus `tid01-turntable.gif`, a captioned looping turntable. All are exported from `docs-site/enclosure.html`, which can also export the mesh as OBJ + MTL or GLB.
- README section linking the rendered documentation and showing the renders.

### Notes
- The renders show a reference model built to the proportions documented here, not Calvin's STL geometry. The printable enclosure remains Calvin's work under CC BY 4.0 and is still not redistributed in this repository.

## [1.1.0] - 2026-06

### Changed
- Expanded `docs/01-protocol.md` substantially: added the separation-of-responsibilities model, template-handling detail, an ASCII channel diagram, a corrected AES-CCM vs AES-GCM comparison table (built-in channel uses CCM, the Magic Keyboard peripheral channel uses GCM), a dedicated secure-intent mechanism explanation, and a forward reference to the threat model. Every claim is now attributed to the Apple Platform Security guide, with inferences explicitly labeled.
- Removed all em-dashes and range en-dashes across the repository in favor of spaced hyphens and plain hyphens, for a consistent plain-text typographic style.

### Added
- Lightning-generation vs USB-C-generation warning in `docs/03-requirements.md` and `docs/04-bom.md`. Apple moved the Magic Keyboard line to USB-C charging on 2024-10-28; the Calvin enclosure targets the Lightning generation, and buyers must verify the port before purchase.
- `CHANGELOG.md` (this file).
- `docs/00-index.md` documentation index with a suggested reading order.

### Verified
- Confirmed model numbers against FCC/Apple designations: A2449 is Magic Keyboard with Touch ID (TKL); A2520 is the Numeric Keypad variant.
- Validated all internal cross-reference links resolve.

## [1.0.0] - 2026-06

### Added
- Initial complete build guide: 11 documentation sections covering protocol, alternatives, requirements, BOM, print plan, teardown, assembly, pairing, threat model, customization, and troubleshooting.
- Ghost in the Shell style project banner (`assets/banner.svg`).
- MIT license for documentation, CC BY 4.0 attribution for Calvin's STL files.
- Full credits to Calvin, GLOUPY, SnazzyLabs, Geerling, and KhaosT.
