# About these files

The four HTML files in this directory are a rendered face of the Markdown in `../docs/`. They exist because a build guide is easier to follow as a page with checklists than as a scroll of Markdown, and because a deck is useful for talking about the project.

They also need explaining, in a repository whose argument is that you should check what you cannot see.

## What is actually in them

Each file is a single self-contained page of roughly 400 to 530 KB. Most of that weight is a base64, gzip-compressed asset bundle carried inline in `<script type="__bundler/manifest">` blocks: seven WOFF2 font faces, the page's own JavaScript, and React 18.3.1 plus ReactDOM.

React is **inlined in the bundle**, not fetched at runtime. These pages open from `file://` with the network off and behave identically. Nothing here calls out.

## How they were produced

They were generated as Claude artifacts and exported. Consequently the bootstrap at the top of each file is host plumbing rather than project code: a `postMessage` relay between frames, blob-URL handling, and workarounds for the artifact host's content security policy. None of it is load-bearing for reading the documentation, and none of it was written for this repository.

That provenance is disclosed for the same reason the rest of the repository attributes its sources. A reader who wants to know where a file came from should not have to reverse-engineer it.

## What this means for you

- **The Markdown in `../docs/` is authoritative.** If these pages and the Markdown ever disagree, the Markdown is right and the disagreement is a bug worth an issue.
- **There is no build step and no source form.** These files cannot currently be regenerated from the Markdown, which means they can drift. Rebuilding them from a real generator, with the Markdown as the single source, is the intended fix and is not done yet.
- **You cannot usefully audit the bundle by reading it.** If that bothers you, and it is a reasonable thing to be bothered by, read the Markdown instead. It loses you nothing but the checkboxes.
- **GitHub serves these as source, not as pages.** Clone the repository and open them from disk, or wait for GitHub Pages to be enabled.
