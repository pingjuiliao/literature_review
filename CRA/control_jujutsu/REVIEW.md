# Control Jujutsu: On the Weaknesses of Fine-Grained Control Flow Integrity∗
- Problem: Coarse-grained enforcements of CFI that use a small number of tags to improve the performance overhead have been shown to be ineffective. As a result, a number of recent efforts have focused on fine-grained enforcement of CFI as it was originally proposed. 
- Method: The work presents Control Jujutsu, that exploits the incompleteness of pointer analysis, when combined with common software engineering practices, to enable an attacker to execute arbitrary malicious code even when fine-grained CFI is enforced.
- Design: The attack uses a new “gadget” class that we call Argument Corruptible Indirect Call Site (ACICS). ACICS gadgets are pairs of Indirect Call Sites (ICS) and target functions that enable Remote Code Execution (RCE) while respecting a CFG enforced using fine-grained CFI.
- Result: The work shows that preventing Control Jujutsu by using more precise pointer analysis algorithms is difficult for real-world applications. In detail, we show that code design patterns for standard software engineering practices such as extensibility, maintainability, and modularity make precise CFG construction difficult.
- Future Work:
  - Analyze more other than DSA algorithm.


### flags
```
{
  "conference": "ACM CCS",
  "year": "2015",
  "keywords": [
    "Code Reuse Attack",
    "CFI"
  ]
}
```
