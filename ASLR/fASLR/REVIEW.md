# fASLR: Function-Based ASLR via TrustZone-M and MPU for Resource-Constrained IoT Systems.
- Problem: porting ASLR to resource-constrained IoT devices is challenging due to limited memory space.
- Method: A trusted runtime randomization engine that validate the entry point of functions and generates the given function body on the randomized region.
- Design:
  - A non-executable application code copy is placed on the unpriviledged address space.
  - Any execution on the non-executable leads to hardware fault and the hardware fault trigger the randomization engine to generaete executable code in randomized address. Note that they perform randomization for each function exactly once. There is no re-randomization.
  - Handling relative/indirect address:
    - direct branches/calls should be replaced with randomized addresses.
    - Indirect branch within functions requires no change, which can adapt to the ramdomized base address.
    - fASLR patched all the relative addressing instruction as direct branches/calls.
      - i.e. -fno-jump-table, -mlong-calls at compile time.
      - Indirect calls/jumps between functions requires instruction patching. 
      - because recalculating all the relative address for indirect calls will incur unacceptable overhead.
  - The randomization engine is trusted and protected via the Trustzone-M
  - fASLR also apply a function desposal mechanism to remove functions that should not be executed anymore from the address space.
    - As ARM binaries do not use frame pointer, they perform frame size analysis to unwind stack.
- Result: The evaluation is tested on CoreMark benchmark, two micro benchmarks Cache Test and Matrix Multiply, nine benchmarks of BEEBS, and eight SAM L11 demo applications obtained from Atmel Start.
  - Preformance: fASLR achieves a high randomization entropy and incurs a runtime overhead of less than 10%.
  - Randomization Entropy: The application that achieves the smallest entropy on average is 80.
    - For the evaluated application, the average is taken different time stamp, since function removal technique is involved.
      - e.g. sometimes there are 5 functions in total, sometimes there are 324 functions in total.
    - This means that there are **2<sup>80</sup>** combinations of function address layouts on average.
      - so, guessing one function's base address could be much less.
  - Memory overhead: For 14 applications evaluated, fASLR achieves less than 5% code size overhead
    - The memory overhead comes from boot engine, randomization engine, and the static function list.
- Future Work:
  - The trampoline method can incur less performance and memory overhead. On top of it, we can make it a rerandomization technique.
  - The authenticated Call Stack mechanism can be used if the performance is acceptable.
  


### flags
```
{
  "conference": "IEEE IoT Journal",
  "year": "2022",
  "keywords": [
    "ASLR",
    "fine-grain ASLR",
    "IoT",
    "ARM Trustzone-M"
  ],
  "Related": [
    "CFI"
  ]
}
```
