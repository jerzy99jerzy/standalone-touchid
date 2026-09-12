# Security policy

## What this repository is

Documentation, plus four generated HTML pages under `docs-site/`. There is no application, no service, and nothing here that processes untrusted input. The realistic security issues are therefore documentation issues, and they matter because people follow this guide while modifying an authentication device.

## What is worth reporting

**Open a public issue** for:

- A security claim that is wrong, overstated, or stated as fact where it is inference. The [threat model](docs/09-threat-model.md) and [protocol analysis](docs/01-protocol.md) are the documents where this matters most.
- A claim attributed to Apple that Apple does not make, or that a current version of the Platform Security guide contradicts.
- Anything in the build or verification procedure that would leave a reader with a weaker device than the guide implies.
- Problems with the bundled pages in `docs-site/`. See [docs-site/README.md](docs-site/README.md) for what is in them.

Public is the right venue for all of the above: nothing here is exploitable against a running system, and a wrong claim is more useful corrected in the open than disclosed privately.

## What this repository cannot act on

Vulnerabilities in Apple's hardware or software. Report those to Apple through [their product security process](https://support.apple.com/en-us/HT201220). If an Apple issue invalidates a claim made here, an issue about the claim is still welcome.

## Scope note for readers

This project documents a physically modified authentication peripheral. Some environments prohibit those categorically, regardless of preserved cryptographic properties, and that is a reasonable policy rather than an oversight. Check yours before building, not after.
