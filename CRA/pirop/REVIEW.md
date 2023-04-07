# Position-independent Code Reuse: On the Effectivenes of ASLR in the Absence of Information Disclosure

- Problem: With all the recetnt work on defeating informatio disclosure, this paper attempts to answer the question: Is it possible to perform code-reuse attacks even without information disclosure.
- Method: PI-ROP leverages the relative position and then overwrites the least significant bytes on the stack to construct a ROP chain without any information leak.
- Result: 
  - expressiveness of PIROP: the work evaluates the availability of gadgets in Asterisk, Apache, Nginx, Lighttpd, and Firefox. The result shows that there is an abundance of gadgets available.
  - effectiveness: for fine-grained randomization techniques, PIROP exploits has low entropy (< 32) on all the exploits. It also shows that function-level randomization can be bypassed.
- Future Work:
  - confined stack frame execution: the scope of variable should be limited by the stack frame so that stack massaging is impossible.


### flags
```
{
  "conference": "Euro S&P",
  "year": "2018",
  "keywords": [
    "CRA",
    "ROP",
    "Temporal safety"
  ]
}
```
