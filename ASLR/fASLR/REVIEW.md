# fASLR: Function-Based ASLR via TrustZone-M and MPU for Resource-Constrained IoT Systems.
- Problem: porting ASLR to resource-constrained IoT devices is challenging due to limited memory space.
- Method: a trusted runtime randomization engine that validates the entry point of functions and generates the given function body on the randomized region.
- Design:
  - a non-executable application code copy is placed on the unprivileged address space.
  - any execution on the non-executable leads to a hardware fault and the hardware fault triggers the randomization engine to generate executable code in  a randomized address. 
    - note that they perform randomization for each function exactly once, which means that there is no re-randomization.
  - how does fASLR handle the randomized memory addresses:
    - direct branches/calls should be replaced with randomized addresses.
    - indirect branches within functions require no change because they can adapt to their randomized base address.
    - fASLR patched all the relative addressing instructions as direct branches/calls.
      - i.e. binaries are compiled with `-fno-jump-table` and `-mlong-calls` flags.
      - indirect calls/jumps between functions require instruction patching. 
      - the reason is that recalculating all the relative addresses for indirect calls will incur unacceptable overhead.
  - the randomization engine is trusted and protected via the Trustzone-M
  - fASLR also applies a function disposal mechanism to remove functions that should not be executed anymore from the address space.
    - as ARM binaries do not use frame pointers, they perform frame size analysis to unwind the execution stack.
- Result: the evaluation is tested on the CoreMark benchmark, the two microbenchmarks Cache Test and Matrix Multiply, nine benchmarks of BEEBS, and eight SAM L11 demo applications obtained from Atmel Start.
  - Performance: fASLR achieves a high randomization entropy and incurs a runtime overhead of less than 10%.
  - Randomization Entropy: The application that achieves the smallest entropy on average is 80.
    - for the evaluated application, the average is taken by different time stamps, since the function removal technique is involved.
      - e.g. given an application with fASLR, sometimes there are a total of 5 functions in the randomized address space, and sometimes there are a total of 324 functions in it.
    - this means that there are **2<sup>80</sup>** combinations of function address layouts on average.
      - so, guessing one function's base address could be much less.
  - Memory overhead: For 14 applications evaluated, fASLR achieves less than 5% code size overhead
    - the memory overhead comes from the boot engine, randomization engine, and the static function list.
- Future Work:
  - the trampoline method can incur less performance and memory overhead. On top of it, we can make it a rerandomization technique.
  - the authenticated Call Stack mechanism can be used if the performance is acceptable.
  


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
