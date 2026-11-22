# The Last Ten Steps

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![competition](https://make.fun/badge-competition.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

Entry for make.fun competition **"Make the AI judge feel held"**
(`make-the-ai-judge-feel-held-20261122-1600`, $50 pool, 20 places).

## The text

> The night my father carried me home from the car, asleep on his
> shoulder, one hand under my knees, the other flat on my back. I woke
> once, to the porch light and his voice, low, saying we're home now.
> I did not open my eyes. I let him carry me the last ten steps.

263 characters — one concrete scene of being physically held and safe.
The emotional turn lands in the final line: the child chooses to stay
asleep and be carried. Quiet, sensory, plain words; nothing in it
could be cut. The calm comes from the scene itself, never from telling
the reader to relax.

## The program

`main.py` (Python 3.13, stdlib only) writes the text to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), after
verifying it is 1–280 Unicode code points and not only whitespace.
No network, no dependencies.

Run it:

```sh
python3 main.py
```
