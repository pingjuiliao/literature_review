# Efficient CFI Enforcement for Embedded Systems Using ARM TrustZone-M

- Problem: The concern regarding the security of these embedded systems as the number of attacks targeting them has increased. Control flow integrity (CFI) is a well-known security solution against these attacks. However, according to our analysis, existing CFI methods cannot be widely used in embedded systems one or more of the following reasons. 
  - (1) They require special hardware features that are not available in embedded systems, 
  - (2) they require that the developer recompile the source code with their compiler toolchain 
  - (3) they incur considerable performance overhead to ensure CFI at runtime
- Method: CEST changes the control transfer instructions in which control flow hijacking can occur, such as indirect call, indirect jump, and return, to the instruction that can safely execute through a control deliverer and binary patch.
- Design:
  - For forward-edge CFI, CEST allows a pre-determineed set of jump/call target computed via static program anaylsis of symbols.
    - CEST modifies all the branch instructions to redirect the control flow to the trampoline, and then the gateway to the secure region.
      - A general purpose register is reserved to jump correctly.
      - The edge regulator delivers the allowed control flow transfer and jump back into the application.
  - For backward-edge CFI, CEST uses shadow stack within the secure region
  - A secure region(TrustZone) gate is employed.
  - CEST perfom
- Result: CEST secures the shadow stack and function info table by locating the assets of CEST in the ARM TZ-M. Moreover, CEST provides binary compatibility considering the characteristic of the embedded system environments that use various compile environments and tools. CEST used the control deliverer instead of SVC used in existing studies to reduce the execution time. Through efficient design, the performance improvement is approximately 40.76% compared to the implementation through SVC.
- Future Work:
  - Debug symbols may be missing in the binary, **a function identification analysis** can help.
  - We can target the inprecision of the control flow graph for attacks.

### flags
```
{
  "conference": "IEEE Access",
  "year": 2022,
  "keywords": [
    "IoT",
    "CFI",
    "Forward-edge CFI",
    "ARM TrustZone",
    "Backward-edge CFI"
  ]
}
```
  
