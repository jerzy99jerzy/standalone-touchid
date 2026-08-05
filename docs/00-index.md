# Documentation index

This is the full documentation set for the Standalone Touch ID build. Read it in order for a first build, or jump to a section by need.

## Suggested reading order

**Before you buy anything:**
1. [Protocol analysis](01-protocol.md) - why this works and what stays intact
2. [Rejected alternatives](02-alternatives.md) - why not an Apple Watch or FIDO2 reader
3. [Requirements](03-requirements.md) - compatibility, the A2449 Lightning-generation caveat, prerequisites
4. [Bill of materials](04-bom.md) - what to buy and roughly what it costs

**Build day:**
5. [3D print plan](05-print-plan.md) - print all four parts first, C plate at 0.10 mm
6. [Teardown guide](06-teardown.md) - open the donor keyboard, four failure points
7. [Assembly](07-assembly.md) - reassemble into the printed enclosure
8. [Pairing](08-pairing.md) - pair with macOS and test

**Reference:**
9. [Threat model](09-threat-model.md) - security posture and residual risk
10. [Customization](10-customization.md) - Ghost in the Shell aesthetic tiers
11. [Troubleshooting](11-troubleshooting.md) - decision tree for failures

## Quick reference

| Fact | Value |
|------|-------|
| Donor keyboard | Magic Keyboard with Touch ID, model A2449, TKL, Lightning generation |
| Target | Any Mac with Apple Silicon (M1 or later) |
| Parts to print | 4 (box, lid, C plate, back plate) |
| Critical print setting | C plate at 0.10 mm layer height |
| Screws | 11x M1.2x4mm, plus 2x M1.2 nuts |
| Session crypto (peripheral channel) | AES-GCM 256-bit, ephemeral ECDH P-256 |
| Total cost | ~$100-150 USD equivalent |
| Total time | 4-6 hours |
