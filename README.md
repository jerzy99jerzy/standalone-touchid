<p align="center">
  <img src="assets/banner.svg" alt="Standalone Touch ID - project banner" width="100%">
</p>

<p align="center">
  <img src="assets/renders/tid01-turntable.gif" alt="TID/01 enclosure, turntable render" width="640">
</p>

<p align="center">
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/docs-v1.3.0-00D9FF?style=flat-square" alt="version"></a>
  <a href="#the-security-question"><img src="https://img.shields.io/badge/focus-threat%20model-9184d9?style=flat-square" alt="focus"></a>
  <a href="docs-site/index.html"><img src="https://img.shields.io/badge/site-interactive%20guide-9184d9?style=flat-square" alt="site"></a>
  <a href="docs/04-bom.md"><img src="https://img.shields.io/badge/cost-~$100--150-e8ede4?style=flat-square" alt="cost"></a>
  <a href="docs/05-print-plan.md"><img src="https://img.shields.io/badge/material-PETG-e8ede4?style=flat-square" alt="material"></a>
  <a href="#prerequisites"><img src="https://img.shields.io/badge/target-Apple%20Silicon-e8ede4?style=flat-square" alt="target"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-00D9FF?style=flat-square" alt="license"></a>
</p>

---

> **A biometric authentication puck for Apple Silicon Macs, built by cannibalizing a Magic Keyboard with Touch ID (A2449) and rehousing its electronics in a 3D-printed enclosure. The interesting part is not the enclosure. It is the claim that rehousing changes nothing the Secure Enclave depends on, and this repository exists to justify that claim rather than assert it.**

**Status:** documentation and analysis. The printable enclosure is [Calvin's work](https://www.printables.com/model/355924) and is not redistributed here. What this repo adds is the protocol analysis, the threat model, sourcing guidance, and a procedure written to be followed.

---

## Why this exists

The MacBook normally lives closed in a Clay vertical dock, driving external displays, with a mechanical keyboard in front of it. That arrangement has one hole in it, and I had stopped noticing the hole years ago.

Then I took the machine away on holiday and used it as a laptop for a week. Touch ID came back. Unlock, `sudo`, Keychain, App Store, all of it without typing a password into a laptop on a hotel desk. Coming home and closing the lid meant giving that up again, and this time the loss was recent enough to be irritating rather than abstract.

Apple's answer is the Magic Keyboard with Touch ID. That is not a fix, it is a trade: you get the sensor by giving up the keyboard you actually want to type on. I am not swapping a mechanical board for a scissor-switch one to recover a fingerprint reader.

So the question narrowed into something better than a shopping problem. The sensor and the keyboard sit in the same shell, but are they in the same trust boundary? If they are not, the sensor can be lifted out without the Secure Enclave noticing or caring. If they are, the whole idea is a downgrade dressed up as a hack.

They are not. The rest of this repository is the work of showing that, and of being honest about the one place where the answer is less comfortable.

---

## The security question

The useful framing of a homebuilt authenticator is not "is this cool" but "what did I just take responsibility for". Here is the trust boundary, layer by layer, with the one thing this build changes marked.

| Layer | Owner | Touched in this build | Consequence |
|---|---|---|---|
| Capacitive sensor, subdermal imaging | Apple silicon | No | Presentation-attack resistance unchanged, for better and worse |
| Channel 1: sensor to PKA block, factory-keyed | Apple, keyed at manufacture | No | Raw ridge data never leaves the board in the clear |
| PKA block and its Apple CA attestation key | Apple silicon | No | A substituted or counterfeit sensor cannot negotiate |
| Channel 2: PKA to Secure Enclave, AES-GCM 256-bit, ephemeral ECDH P-256 | Negotiated at pairing | No | The cable is a dumb carrier for ciphertext |
| Secure intent line, button to Secure Enclave | Apple, dedicated hardware path | No, original button carried over | No software-forgeable press exists |
| Template storage, matching, policy | Your Mac's Secure Enclave | No, never in the puck at all | Re-pairing to another Mac means enrolling again |
| Mechanical enclosure, click path, ESD exposure during assembly | **You** | **Yes, entirely** | This is the whole delta |

The last row is the project. Everything above it is untouched Apple silicon doing what it did in the original shell. The derivation, with every claim attributed to Apple's Platform Security guide, is in [Protocol analysis](docs/01-protocol.md).

### Threat model, at a glance

| Attack class | Factory keyboard | This build |
|---|---|---|
| Cable tap, malicious dock, in-line MITM | Authenticated ciphertext and metadata only | Same |
| Counterfeit device substitution | Refused at pairing, Apple CA attestation | Same |
| Lifted print, mould, photograph | Resists casual attempts, has fallen to lab work | Same, unchanged in either direction |
| Malware authorizing `sudo` or Apple Pay | Blocked by the secure intent hardware path | Same |
| **Tampered but genuine donor logic board** | Not applicable, bought sealed | **New. See below** |
| Coercion, macOS compromised below the prompt | Out of scope | Out of scope |

Five rows come out identical because the mechanism producing them is identical. One row is new, and it arrives for a procurement reason rather than a cryptographic one. Full treatment in [Threat model](docs/09-threat-model.md).

### The one new risk: a used authenticator

A factory keyboard arrives sealed. This build starts by buying a used authentication peripheral from a marketplace, which is a different proposition and deserves saying out loud rather than burying in section nine.

Apple CA attestation defends the biometric channel. A substituted PKA block will not pair, so the classic counterfeit-hardware attack is closed at the protocol level. Attestation does not reach further than that. The donor logic board is carried over whole, and *[inference, not verified against a built unit]* its HID keyboard interface should still enumerate even with the key matrix gone. A donor carrying an implant on that path would be a keystroke injection surface, and the Touch ID protocol would have nothing to say about it, because HID is not part of the attested channel.

Practical handling:

- Buy from sellers with history and a return path. Price is the wrong variable to optimise on a device whose entire function is authorization.
- **Model number and port must agree.** The generations carry disjoint numbers, so a mismatch is not a careless seller, it is a device whose label does not describe its hardware.

| Generation | Touch ID, TKL | Touch ID with numeric keypad |
|---|---|---|
| Lightning, 2021 | **A2449, the donor this build requires** | A2520 |
| USB-C, late 2024 | A3118 | A3119 |

- Inspect the adhesive seam. Factory bonding is uniform and a prior entry usually shows at the edges.
- You are going to open the thing anyway, which is a tamper inspection nobody buying a factory keyboard gets. Photograph the internals before touching anything.
- Confirm what actually enumerates before you enrol a finger.

### Verifying your own unit

This repository argues that the security posture survives. You should not take that on trust for the object on your desk, so the guide ends with a read-only check rather than a congratulation:

```bash
system_profiler SPUSBDataType | grep -i -B2 -A10 "keyboard"
ioreg -p IOUSB -w0 -l | grep -i -E "USB Product Name|idVendor|idProduct"
```

You are confirming that the device reports under Apple's vendor ID as the keyboard it claims to be, that exactly one HID interface shows up and you can account for it, and that a single physical press authorizes exactly one `sudo`. Full procedure, including what to capture as a known-good baseline, in [pairing 8.6](docs/08-pairing.md#86-verifying-what-you-built).

---

## What this repo is

Documentation. A build guide with sourcing, per-part print settings, a teardown procedure with the failure points called out, the assembly sequence, macOS pairing and verification, a threat model, and finish notes. Written to be read straight through once, then referenced with sticky fingers during the build.

## What this repo is not

A distribution of the 3D model files. The STLs are Calvin's and live on [Printables](https://www.printables.com/model/355924). Download them from source; check the license shown there before remixing. This repo links, credits, and documents around them.

## Epistemic discipline

Every cryptographic claim in [Protocol analysis](docs/01-protocol.md) is attributed to Apple's Platform Security guide. Where this repository reasons past what Apple states, it says `Inference:` in the text. Where a claim rests on an expectation about this build that nobody has tested, it is marked in brackets where it appears. Where a number circulates widely but could not be traced to a source, it is recorded as untraced rather than quietly repeated.

That labeling is the point. A build guide claiming "the security is unchanged" without separating the documented from the inferred from the assumed is asking for trust it has not earned. An unlabeled inference in here is a bug, and an issue about one is welcome.

---

## Documentation

| # | Document | Contents |
|---|----------|----------|
| 0 | [Documentation index](docs/00-index.md) | Reading order and quick-reference table |
| 1 | [Protocol analysis](docs/01-protocol.md) | Apple's Touch ID cryptographic architecture: PKA block, attestation, AES-GCM session, secure intent |
| 2 | [Rejected alternatives](docs/02-alternatives.md) | Why Apple Watch fails as a desk authenticator, why FIDO2 readers do not replace Touch ID |
| 3 | [Requirements](docs/03-requirements.md) | Model matrix, the Lightning-generation constraint, prerequisites |
| 4 | [Bill of materials](docs/04-bom.md) | Donor sourcing, filament, hardware, tools, cost |
| 5 | [3D print plan](docs/05-print-plan.md) | Per-part slicer settings from Calvin's notes, PETG parameters, orientation, post-processing |
| 6 | [Teardown guide](docs/06-teardown.md) | Disassembly, four failure points, parts to keep, Li-Po handling |
| 7 | [Assembly](docs/07-assembly.md) | Step-by-step assembly into the printed enclosure |
| 8 | [Pairing and verification](docs/08-pairing.md) | macOS pairing, functional test, and the read-only checks worth running first |
| 9 | [Threat model](docs/09-threat-model.md) | Transport, supply chain, liveness, residual risk, and what sits outside the boundary |
| 10 | [Customization](docs/10-customization.md) | Finish work, four tiers, and which ones are worth the time |
| 11 | [Troubleshooting](docs/11-troubleshooting.md) | Decision tree for print, teardown, and pairing failures |

---

## Rendered documentation

The same documentation, rendered. Each page is self-contained: no build step, no network access at runtime.

> **Two notes.** GitHub serves `.html` from a repository as source rather than as a page, so clone and open these from disk, or read them on the published site once Pages is enabled. And see [docs-site/README.md](docs-site/README.md) for how these files were produced and what is inside them, which matters more than usual in a repository about trusting what you cannot see.

| | |
|---|---|
| **[Interactive build guide](docs-site/index.html)** | Every section on one page, with print, teardown, assembly and pairing checklists that remember where you stopped |
| **[Project deck](docs-site/deck.html)** | Fifteen slides with speaker notes, for a talk or a write-up |
| **[Printable guide](docs-site/print.html)** | The same build paginated for paper; print to PDF from the browser |
| **[3D enclosure viewer](docs-site/enclosure.html)** | Reference model of the box, lid, C plate and back plate: orbit, explode, toggle dimensions, export OBJ + MTL or GLB |

| Plan | Exploded |
|------|----------|
| ![Plan view](assets/renders/tid01-top.png) | ![Exploded view](assets/renders/tid01-exploded.png) |

### Dimensions

![Plan with dimensions](assets/renders/tid01-dimensions-plan.png)

![Elevation with dimensions](assets/renders/tid01-dimensions-elevation.png)

> The renders and the turntable show a reference model built to the documented
> proportions, not Calvin's STL geometry. The printable enclosure is
> [Printables 355924](https://www.printables.com/model/355924) by
> [Calvin](https://www.printables.com/@Calvin_5743) and is not redistributed here.

---

## Build in one paragraph

Buy a used Magic Keyboard with Touch ID, model A2449, the tenkeyless Lightning generation. Print four parts in PETG from [Calvin's model](https://www.printables.com/model/355924), three at 0.20 mm layer height and the C plate at 0.10 mm, which is the one setting with no room in it. Open the keyboard by softening the adhesive at 60-65°C and prying slowly; the Touch ID flex cable and the Li-Po cell are the two things you can destroy for good. Keep the logic board, the Lightning port, the Touch ID button with its ribbon, and the spring plate with its four screws. Reassemble inside the printed enclosure with eleven M1.2x4mm screws and two M1.2 nuts. Connect over USB-C to Lightning to any Apple Silicon Mac, pair through System Settings > Touch ID & Password, run the verification block, then enrol a finger. Four to six hours, $100-150 USD equivalent.

---

## Prerequisites

- **Mac with Apple Silicon** (M1 or later). Apple does not support Magic Keyboard Touch ID on Intel Macs, T2 or otherwise.
- **FDM 3D printer** with a heated bed reaching 75-85°C and capable of 0.10 mm layers. Prusa MK3S/MK4, Bambu A1/P1/X1, Voron 2.4, Creality K1, Sovol SV06+ all qualify.
- **Willingness to destructively disassemble** a Magic Keyboard. There is no clean way back.
- **PETG filament.** See the [BOM](docs/04-bom.md).
- **Basic electronics repair skills.** No soldering, but you will handle flex PCB and mm-scale screws.

---

## Credits

This project is documentation around other people's work. The lineage, per the model origin data on Printables:

- **[Calvin](https://www.printables.com/@Calvin_5743)** - [Clickable Touch ID Box (TKL board, wired)](https://www.printables.com/model/355924). The enclosure this build uses, and the primary source for print settings and assembly order. Calvin's box is a remix of SnazzyLabs' model, with the click mechanism credited to GLOUPY.
- **[SnazzyLabs](https://www.printables.com/model/320000)** - the original standalone Touch ID module, and the main design Calvin remixed. Also the [video](https://www.youtube.com/watch?v=hz9Ek6fxX48) that started the whole thread.
- **[GLOUPY](https://www.printables.com/model/349777)** - the clickable button mechanism that Calvin's C plate draws on.
- **[Jeff Geerling](https://www.jeffgeerling.com/blog/2025/why-doesnt-apple-make-standalone-touch-id/)** - one documented build start to finish, the source of several warnings reproduced here, and the direct prompt for this English-language guide.
- **[KhaosT](https://gist.github.com/KhaosT/1406a6b6bea38f59e059c2afcb39d545)** - the teardown notes Calvin's own instructions point at.

Full attribution, including sources credited inside Calvin's comment thread, in [CREDITS.md](CREDITS.md). If this repo is useful to you, credit the people above before crediting the documentation.

## License

Documentation here is [MIT](LICENSE). Calvin's STL files are licensed separately on Printables and are not redistributed; check the license shown on the model page before reusing them.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Two contributions are worth more than everything else: a documented build report from your own attempt, and any claim in here you can show is wrong, unsourced, or labeled as fact when it is not.

## Disclaimer

You will destroy an Apple product. You may cut yourself, burn yourself, or set a lithium-polymer battery on fire. This documentation is provided as is, with no warranty of any kind. Apple supports none of it, and some regulated environments will reject a physically modified authenticator regardless of what survived the modification.

---

<p align="center">
  <sub>公安9課製 · TID/01 · Stand Alone Complex</sub>
</p>
