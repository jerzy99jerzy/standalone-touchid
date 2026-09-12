# Contributing

This is a documentation repository. Corrections are the main currency.

## The two most valuable contributions

**A build report.** Nobody has yet published a build from this guide, including its author, and the guide is weaker for it. If you build one, open a build report issue with your printer, filament, donor model and port, whether the C plate clicked on the first print, and what the guide got wrong. Photographs of a real unit are worth more than every render in this repository.

**A claim you can show is wrong.** Specifically: a statement presented as fact that is inference, a number that cannot be traced to a source, an attribution to the wrong person, or a security property stated more strongly than the evidence supports. These are the defects this repository most wants to find, and finding one is not an inconvenience.

## House rules

- **Attribute claims.** Architecture claims trace to Apple's Platform Security guide. Build claims trace to Calvin's model page first, then to other documented builds. Anything reasoned out rather than sourced is marked `Inference:` or bracketed where it appears.
- **Do not repeat untraced numbers.** If a figure circulates widely but nobody can point at its origin, label it untraced. There is at least one such figure in here already, marked as such.
- **Do not redistribute the STL files.** They are Calvin's, hosted on Printables. Link to the source.
- **No em-dashes or en-dashes** in authored files. Spaced hyphens instead. This is a house style rule and CI enforces it across the tree, with `docs-site/` exempt because those files are generated.
- **The Markdown in `docs/` is the source of truth.** `docs-site/` is a rendered copy that cannot currently be regenerated; if the two disagree, fix the Markdown and say so in the issue.
- **Prices and market claims get a date.** They drift faster than anything else here.

## Practical

Small corrections: open a pull request directly. Anything that changes a security claim, an attribution, or the build procedure: open an issue first so the sourcing can be discussed before the wording. Update `CHANGELOG.md` in the same change.
