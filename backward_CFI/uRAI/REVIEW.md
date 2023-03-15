# µRAI: Securing Embedded Systems with Return Address Integrity 
- Problem: Control-flow hijacking targeting the backward edge (e.g., Return-Oriented Programming–ROP) remains a threat for Microcontroller-based systems(MCUS). Current defenses are either susceptible to ROP-style attacks or require special hardware such as a Trusted Execution Environment (TEE) that is not commonly available on MCUS.
- Method: a compiler-based mitigation to prevent control-flow hijacking attacks targeting backward edges by enforcing the Return Address Integrity (RAI) property on MCUS. µRAI inserts a list of direct jumps in the code region of each function (i.e., in R+X memory), where each jump corresponds to a possible return target (i.e., a call site) for the function. 
- Design: 
  - uRAI compiles a list of possible return address and assign them with hard-coded IDs. Instead of using return address, the ID is used for lookup of the list
    - Reserving a general purpose register, named State Register (SR), which corresponds to current return address ID.
    - before calling any function, the SR will XOR the assigned hard-coded ID associated with the return address.
    - at each return, a return address lookup is performed via *lookup_table[SR]*
    - after returning from a function, the SR is XORed again to set SR back to current function.
    - indirect calls are handled via allowed set of jump targets in the table.
  - Exception handlers execute in privileged mode, and can execute asynchronously. Therefore, enforcing the RAI property for a function called within an exception handler requires more than just protecting return addresses. To overcome this limitation, µRAI enforces SFI on sensitive privileged Memory Mapped I/O (MMIO) such as the MPU, in addition to encoding SR. Enforcing SFI within an exception handler context only has negligible overhead since these are only a limited portion of the entire application.
- Limitation:
  - path explosion problem could blow up the list of return addresses.
- Result: The RAI property ensures absence of control flow hijacking without requiring special hardware extensions. 
  - Return address is fully protected since 
  - We evaluate µRAI on five representative MCUS applications (PinLock, FatFs-RAM, FatFs-uSD, LCD-uSD, and Animation) and the CoreMark benchmark. µRAI shows an average overhead of 0.1%.
- Future Work:
  - Find some exemplary programs in MCUS that its list of return addresses cannot be determined.

### flags
```
{
  "conference": "NDSS",
  "year": "2020",
  "keywords": [
    "IoT",
    "Backward-edge CFI",
    "CFI"    
  ]
}
```
