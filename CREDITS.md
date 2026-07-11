# Credits

This project is documentation around work by others. It does not distribute any of the primary artifacts (STL files, videos, code) — those live at their sources, linked below.

## 3D model — the primary artifact

**[Calvin (@Calvin_5743 on Printables)](https://www.printables.com/@Calvin_5743)**

- Model: [Clickable Touch ID Box (TKL board, wired)](https://www.printables.com/model/355924)
- License: CC BY 4.0 (per Printables policy)
- Every dimension, tolerance, and mechanical design decision in the enclosure is Calvin's work
- Calvin remixed and improved on GLOUPY's earlier clickable box, which itself derived from SnazzyLabs' original standalone Touch ID module concept

**Editable in Tinkercad:** [https://www.tinkercad.com/things/20VXvaGcfWs-touch-id-box](https://www.tinkercad.com/things/20VXvaGcfWs-touch-id-box)

## Predecessor models and concepts

**SnazzyLabs**
- Original standalone Touch ID module concept
- [YouTube: Standalone Touch ID — proof of concept](https://www.youtube.com/watch?v=hz9Ek6fxX48)
- [Printables: Standalone Touch ID Module for Mac](https://www.printables.com/model/320000)

**GLOUPY**
- Original clickable button mechanism (the C plate concept)
- [Printables: Touch ID Box with Button Press](https://www.printables.com/model/349777)

## Documentation and popularization

**Jeff Geerling**
- [Blog post: "Why doesn't Apple make a standalone Touch ID?"](https://www.jeffgeerling.com/blog/2025/why-doesnt-apple-make-standalone-touch-id) — the direct inspiration for this English documentation effort
- [YouTube build video](https://www.youtube.com/watch?v=tzB6m2VTxAg)
- Jeff's writeup documented the specific 0.10 mm vs 0.12 mm layer height issue for the C plate, which this guide reproduces prominently

## Teardown reference

**KhaosT**
- [Gist: Magic Keyboard with Touch ID teardown notes](https://gist.github.com/KhaosT/1406a6b6bea38f59e059c2afcb39d545)
- Early reference for the disassembly procedure

## Apple documentation

Apple's Platform Security guide is the canonical reference for the cryptographic architecture described in [Protocol analysis](docs/01-protocol.md):

- [Magic Keyboard with Touch ID](https://support.apple.com/guide/security/magic-keyboard-with-touch-id-secf60513daa/web)
- [Biometric security](https://support.apple.com/guide/security/biometric-security-sec067eb0c9e/web)
- [Secure intent and connections to the Secure Enclave](https://support.apple.com/guide/security/secure-intent-connections-enclave-sec7a94f7d1e/web)

## This documentation

Original English documentation, sourcing analysis, threat model synthesis, and customization direction in this repository are original work released under the [MIT License](LICENSE).

If you find this useful, credit the primary makers above (Calvin, GLOUPY, SnazzyLabs, Geerling) before crediting this documentation repo.
