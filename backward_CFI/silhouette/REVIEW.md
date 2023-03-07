# Silhouette: Efficient Proteceted Shadow Stacks for Embedded Systems

- Problem: control-flow hijacking remains a prevalent threat in embedded systmes due to resource and execution-tie constraints.
- Method:
  - enforced a coarse-grained CFI along with a parallel shadow stack.
  - modify all regular "store" instructions to "unprivileged store" instructions, except for the ones used for the shadow stack.
  - adopted a code scanner for other privileged instructions.
  - devised Sihouette-Invert at the cost of minor hardware change.
- Result: Silhouette incutrs a geometric mean of 1.3% and 3.4% performance overhead, and a geometric mean of 8.9 and 2.3% code size overhead on the CoreMark-Pro qand BEEBs benchmark suites, resepctively.
- Future Work:
  - Memory-efficient shadow stack for embedded systems
  - Extend the unprivileged move to more powerful protection mechanism such as CPI.

### flags

```
{
  "conference": "USENIX",
  "year": "2020",
  "keywords": [
    "Backward-edge CFI",
    "Shadow Stack",
    "CFI",
    "ARM",
    "ARMv7-M"
  ]
}
```
