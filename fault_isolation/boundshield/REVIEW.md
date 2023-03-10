# BoundShield: Comprehensive Mitigation for Memory Disclosure Attacks via Secret Region Isolation

- Problem: fine-grained ASLR can be bypassed by exploiting memory corruption vulnerabilities and performing memory disclosure attacks. Although XoM schemes have been proven to be an efficient solution against read-based memory disclosures, existing solutions need modifications to kernel or hypervisor. Besides, the defense of execution-based memory disclosures has been ignored.
- Method: divide the user address space into two regions with a SFI-based mechanism, and use the secret region to hide code sections and code pointers in the memory
- Design: (this work is essentially CPI with Intel MPX)
  - BoundShield divides address space into a secret region and a regular region via Intel MPX. Sensitive data, such as code and code pointers, are stored in the safe region.
  - For all load/store instrucitons, MPX enforces a bound-checking policy via MPX "bndcl"/"bndch" instructions except for the instructions that are allowed for storing such sensitive informations. (privileged vs. unprivileged store).
  - Until this point, some code pointers are required to store on the execution stack/heap/data region, which are vulnerable to execution-based memory disclosure, i.e. redirecting the control flow to these code pointer (with offsets) to see what happes.
  - The safe region can be further divided into code region and trampoline region(via MPX). The trampoline serves as an indirect layer so that the code pointer on the regular(unsafe) region can only be the code pointer to the trampoline, mitigates the execution-based memory disclosure.
  - Since ASLR hides the code region, execution-based memory disclosure has low chance of getting into the middle of code region.
  - BoundShield also uses a another stack in the safe region to protect the return addresses. (which is essentially Shadow Stack).
  - According to the previous work, the standard use of MPX imposes a significant runtime overhead (over 2× on SPEC benchmarks). However, previous works have shown that the vast impact on performance is mainly introduced by repeatedly loading and storing bounds rather than performing bound check instructions, which often takes little performance overhead.
  - BoundShield stops read-based memory disclosures by hiding all code sections and code pointers in the secret region.
  - Meanwhile, BoundShield stops execution-based memory disclosures by preventing return addresses from being corrupted and checking whether function pointers point to legitimate entries when they are dereferenced.
- Result: BoundShield only incurs minor overhead, in details, 5.8% slowdown for SPEC CPU2006 benchmarks on average. Moreover, BoundShield does not require any OSlevel or hypervisor-level modifications and can be readily adopted to defend more complex attacks.
- Future Work:
  - MPX + The trampoline mechanism limited execution-based memory disclosure.
    - full function reuse is still possible.
    - execution-based memory disclosure is frustrated by information hiding.
  - Problem with MPX
    - say, the program let user input an integer, MPX should not bound-checking that.
    - However, if not checking, we are leaving an effective code pointer on the stack.
  - the bound checking mechanism can be exploited to reduce the entropy of code region.
    - we can probably learn the upper-bound and the-lower bound by control-flow hijacking
  - the Same model using Intel CET since that MPX is not supported.


### flags
```
{
  "conference": "IEEE Access",
  "year": "2018",
  "keywords": [
    "Fault Isolation",
    "Intel MPX",
    "Trampoline"
  ],
  "Complementary": [
    "ASLR",
    "Shadow Stack"
  ],
  "Related": [
    "XoM"
  ]
}
```
