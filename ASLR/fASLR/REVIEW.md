# fASLR: Function-Based ASLR via TrustZone-M and MPU for Resource-Constrained IoT Systems.
- Problem: porting ASLR to resource-constrained IoT devices is challenging due to limited memory space.
- Method: A trusted runtime randomization engine that validate the entry point of functions and generates the given function body on the randomized region.
- Design:
  - A non-executable application code copy is placed on the unpriviledged address space.
  - Execution on the non-executable leads to hardware fault and the hardware fault trigger the randomization engine to generaete executable code in randomized address. Note that they perform randomization for each function exactly once. There is no re-randomization
  - It is difficult for fASLR to handle indirect call, so the application should be compiled without using indirect addressing.
  - fASLR does not re-randomize the called function address. Instead, they rewrite the call instruction to perform 
  - The randomization engine is trusted and protected via the Trustzone-M
  - fASLR also apply a function desposal mechanism to remove functions that should not be executed anymore from the address space.
- Result: fASLR achieves a high randomization entropy and incurs a runtime overhead of less than 10%. Furthermore, it achieves 5% code size overhead.
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
