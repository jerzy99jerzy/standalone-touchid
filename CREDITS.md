# Credits

This project is documentation around work by others. It does not distribute any of the primary artifacts (STL files, videos, code) - those live at their sources, linked below.

## 3D model - the primary artifact

**[Calvin (@Calvin_5743 on Printables)](https://www.printables.com/@Calvin_5743)**

- Model: [Clickable Touch ID Box (TKL board, wired)](https://www.printables.com/model/355924)
- Every dimension, tolerance, and mechanical design decision in the enclosure is Calvin's work
- Lineage, per the model origin block on the Printables page: Calvin's box is a **remix of SnazzyLabs' model 320000**, which supplied the main design. The click mechanism is separately credited there as inspired by GLOUPY's model 349777. Calvin's own listed changes over SnazzyLabs are a centred Touch ID button, the click action, and the removal of glue, supports, brass inserts, and board drilling.
- **License:** check the license shown on the model page before reusing or redistributing anything from it. This repository does not redistribute the STLs, so the question does not arise here, but it will for anyone remixing.

**Editable in Tinkercad:** [https://www.tinkercad.com/things/20VXvaGcfWs-touch-id-box](https://www.tinkercad.com/things/20VXvaGcfWs-touch-id-box)

## Upstream models

**SnazzyLabs**
- Original standalone Touch ID module concept, and the main design Calvin's box remixes
- [Printables: Standalone Touch ID Module for Mac](https://www.printables.com/model/320000)
- [YouTube: Standalone Touch ID - proof of concept](https://www.youtube.com/watch?v=hz9Ek6fxX48). Calvin links [the keycap-removal moment at 6:14](https://youtu.be/hz9Ek6fxX48?t=374) as the reference for that step.

**GLOUPY**
- The clickable button mechanism that inspired Calvin's C plate
- [Printables: Touch ID Box with Button Press](https://www.printables.com/model/349777)

## Documentation and popularization

**Jeff Geerling**
- [Blog post: "Why doesn't Apple make a standalone Touch ID?"](https://www.jeffgeerling.com/blog/2025/why-doesnt-apple-make-standalone-touch-id) - the direct inspiration for this English documentation effort
- [YouTube build video](https://www.youtube.com/watch?v=tzB6m2VTxAg)
- Jeff reported reprinting a plate at 0.1 mm after his slicer default of 0.12 mm left it sitting too high. He calls the part the "Touch ID backing plate"; Calvin's instructions put the 0.1 mm requirement on the C plate, and Calvin is the primary source this guide follows
- Jeff's build is also the source for the nut-balancing technique in [Assembly](docs/07-assembly.md) and the 50/50 assessment of the Touch ID flex cable in [Teardown](docs/06-teardown.md)

## Teardown references

**KhaosT**
- [Gist: Magic Keyboard with Touch ID teardown notes](https://gist.github.com/KhaosT/1406a6b6bea38f59e059c2afcb39d545)
- Early reference for the disassembly procedure, and the guide Calvin links from step 1 of his instructions

**Disassembly video linked by Calvin**
- [youtube.com/watch?v=5h-i6v3eVqM](https://www.youtube.com/watch?v=5h-i6v3eVqM), the second teardown reference in Calvin's step 1

**@Seth_10131**
- Suggested heating the back of the keyboard on a 3D printer bed, in the comments on Calvin's model. That is the method this guide recommends first in [Teardown](docs/06-teardown.md)

## Apple documentation

Apple's Platform Security guide is the canonical reference for the cryptographic architecture described in [Protocol analysis](docs/01-protocol.md):

- [Magic Keyboard with Touch ID](https://support.apple.com/guide/security/magic-keyboard-with-touch-id-secf60513daa/web)
- [Biometric security](https://support.apple.com/guide/security/biometric-security-sec067eb0c9e/web)
- [Secure intent and connections to the Secure Enclave](https://support.apple.com/guide/security/secure-intent-connections-enclave-sec7a94f7d1e/web)

## This documentation

Original English documentation, sourcing analysis, threat model synthesis, and customization direction in this repository are original work released under the [MIT License](LICENSE).

If you find this useful, credit the primary makers above (Calvin, GLOUPY, SnazzyLabs, Geerling) before crediting this documentation repo.
