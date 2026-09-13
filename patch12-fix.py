"""Patch 12 fix: two mutants that patch 12 took off their targets, and the
invariant one of them stopped defending on the map a reader gets.

`python tools/mutation_run.py --write-hints` reported two survivors and
neither is a hole in the code. Both are the same failure as patch 10's
`crossings-drawn-over-the-alert-markers`: a mutant's target text is a claim
about a line, and a patch that edits the line silently disarms the mutant
while the gate stays green on everything else.

1. `the-tiled-alert-circles-go-back-to-being-decoration` aims at
   `clickable: true\\n      });`. Patch 12 appended `zIndex: 3` after
   `clickable: true`, so the target no longer exists. Repaired by moving the
   new key above the old one rather than by rewriting a mutant that has been
   red for many releases: the object is unordered, the mutant is not.

2. `a-communique-paints-poland-quiet-instead-of-leaving-it-unpainted` aims at
   the guard that paints only a named voivodeship. Patch 12's
   `syncWarningShapes` copied that guard onto the tiled map verbatim, so the
   target now occurs twice and `replace(..., 1)` edits whichever comes first
   in the file, which is not the line the mutant names. Repaired by giving the
   new loop its own variable, so the old target is unique again and still aims
   at the drawing.

3. That leaves the tiled map's copy of the guard undefended, which is D-S28's
   own shape and the reason this release exists: an invariant proved on the
   map local development renders and not on the map production serves. A third
   mutant is registered for it. It dies to `the communiques reach the tiled
   map at all`, which counts two polygons against a fixture naming two
   voivodeships; without the guard all sixteen are drawn.

Run from the repository root, after patch12.py.
"""
from __future__ import annotations

import pathlib
import sys

APPLIED: list[str] = []


def sub(path: str, old: str, new: str, label: str) -> None:
    p = pathlib.Path(path)
    if not p.exists():
        sys.exit(f"MISSING {path}: run this from the repository root")
    text = p.read_text()
    n = text.count(old)
    if n != 1:
        sys.exit(f"ANCHOR {label}: {n} matches in {path}, expected 1")
    p.write_text(text.replace(old, new, 1))
    APPLIED.append(label)


MAP = "src/mavosite/map.py"
MUT = "tools/mutation_run.py"

# ------------------- 1. the alert circle keeps `clickable` last

sub(MAP, '''        fillOpacity: active ? 0.18 : 0.06,
        clickable: true,
        // Stated rather than left to insertion order, now that three layers
        // share this map: communiques at 0, the archive's rings and marks at
        // 1 and 2, and what is happening now on top. `syncWarningShapes` can
        // run at any moment, so "added later" is not an ordering.
        zIndex: 3
      });''',
    '''        fillOpacity: active ? 0.18 : 0.06,
        // Stated rather than left to insertion order, now that three layers
        // share this map: communiques at 0, the archive's rings and marks at
        // 1 and 2, and what is happening now on top. `syncWarningShapes` can
        // run at any moment, so "added later" is not an ordering.
        //
        // **Written above the click flag on purpose.** The object is
        // unordered and the mutation register is not: a mutant has aimed at
        // that flag followed by the closing brace since D-S50, and a key
        // appended after it reports "target string not found", which is a
        // disarmed mutant wearing the face of a passing gate.
        zIndex: 3,
        clickable: true
      });''', "the alert circle keeps clickable last")

# ------------- 2. the tiled loop stops shadowing the drawing's guard

sub(MAP, '''    var map = window.__mavoMap, vslug, rings;''',
    '''    // `wslug` rather than `vslug`, which the drawing's own loop uses. The
    // two loops are the same idea on two base maps and the mutation register
    // addresses each by its text, so one name in both places makes one
    // mutant's target ambiguous and the other's unwritable.
    var map = window.__mavoMap, wslug, rings;''',
    "the tiled loop names its own variable")

sub(MAP, '''    for (vslug in geo.voivodeships) {
      if (!warnedVoivodeships[vslug]) { continue; }
      rings = geo.voivodeships[vslug].map(function (ring) {''',
    '''    for (wslug in geo.voivodeships) {
      if (!warnedVoivodeships[wslug]) { continue; }
      rings = geo.voivodeships[wslug].map(function (ring) {''',
    "the tiled loop reads its own variable")

# --------------------- 3. the same invariant, on the tiled map

sub(MUT, '''        edits=(("src/mavosite/map.py",
                "      if (!warnedVoivodeships[vslug]) { continue; }\\n",
                ""),),
    ),''',
    '''        edits=(("src/mavosite/map.py",
                "      if (!warnedVoivodeships[vslug]) { continue; }\\n",
                ""),),
    ),
    # The same claim, on the map production serves. The one above defends the
    # drawing and defended only the drawing for as long as the layer existed,
    # which is F-S89 restated as a hole in the register rather than in the
    # code: an invariant is proved on both base maps in the same release or on
    # neither (D-S28). Dies to `the communiques reach the tiled map at all`,
    # which counts two polygons against a fixture that names two
    # voivodeships; with the guard gone all sixteen are drawn.
    Mutant(
        "the-tiled-communique-layer-paints-every-voivodeship",
        "an unpainted voivodeship says this build checked nothing; a fill "
        "over all sixteen says Poland was checked and found warned, which is "
        "a claim nobody made. The drawn map has defended this since D-S53 and "
        "the tiled map is the one a reader gets",
        edits=(("src/mavosite/map.py",
                "      if (!warnedVoivodeships[wslug]) { continue; }\\n",
                ""),),
    ),''', "the tiled guard joins the register")

print(f"applied: {len(APPLIED)}")
for label in APPLIED:
    print(f"  - {label}")
