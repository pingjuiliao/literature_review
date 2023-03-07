# MARDU: Efficient and Scalable Code Re-randomization

- Problem: While code reuse attacks evolves in complexity, defenses designs are neither practical nor scalable.
- Method: a system-wide re-randomization-on-crash mechanism to provide a scalable scheme to prevent attackers from harvesting code reuse gadget, which supports code sharing for compatibility.
- Challenge: 
  - having fine-grained ASLR with re-randomization while not sacrificing performance.
- Design:
  - MARDU fine-grained the randomization in function level.
  - MARDU application must go through a trampolines region to enter into or return from a function. The trampoline mechanism exists for several reasons:
    - First, it requires no runtime tracking for rerandomization.
    - Second, it hides the code pointer in the real code region. (but the trampoline addresses are exposed) 
    - Third, since trampoline and code regions are seperated, XoM can be enable for the code region.
    - return address (code pointers to the trampoline region) can still be enabled.
  - One process, instead of per-process, is dedicated to preform re-randomization for the entire system.
  - MARDU only performs re-randomization while detect malicious behavior on crash, flushing attackers knowledge while attackers cannot trigger a crash.
  - MARDU modified kernel to manage code cache for randomized code so that the code can be shared.
- Result: MARDU incurs 5.5% and 4.4% performance overhead in SPEC 2006 and nginx respectively, confirming practicality and scalability.
- Future work:
  - Since the trampoline addresses are stationary, the full function reuse can be a good attack surface. 
    - CFI to prevent the full function reuse of MARDU application. 
    - perform static analysis that prevents the linked modules from doing malicious things.
  - side-channel attack via hardware.



### flags

```
{
  "conference": "SYSTOR",
  "year": "2020",
  "keywords": [
    "Rerandomization", 
    "ASLR",
    "Fine-grain ASLR",
    "Intel MPK"
  ],
  "complementary": [
    "Xom",
    "Shadow Stack"
  ]
}
```
