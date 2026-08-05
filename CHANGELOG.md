# Changelog

All notable changes to this documentation are recorded here. This project versions the documentation, not a software release; "version" means a coherent state of the build guide.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) loosely, adapted for a documentation repo.

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
