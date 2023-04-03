# Dynamic and Secure Memory Transformation in Userspace
- Problem: while continuous code re-randomization mitigates attack, exists approaches do not achieve strong isolation nor defend against novel attack. Specifically, PIROP abuse stack leftovers to construct attack payload.
- Method: this paper present, Chameleon, a userspace frameowkr that timely permutes the stack slot layout and code 
- Design:
  - Chameleon spawn an evert handling thread waits for interrupts. The thread contains a event handler, a scrambler, and a fault handler and respond for re-randomization of the target process. The separated process serves as a strong isolaotion mechanism, which handles the following process:
    - Chameleon permutes the ordering and adds random amount of pading between slots.
    - Chameleon rewrite the code layout with trap instructions inbetween 
- Result: The evaluation shows Chameleon significantly raises the bar of stack object related attacks with only a 1.1% overhead when re-randomizing every 50 ms.
- Limitations: 
  - Chameleon incurs huge overhead if it re-randomize code and stack per 10 ms.
  - The work applies the re-randomization merely on the code and stack region while incur non-negligible overhead in practice.
- Future work:
  - defends against PIROP.
    - stack/base pointer integrity.
    - new design of execution stack.

### flags
```
{
  "conference": "ESORICS",
  "year": "2020",
  "keywords": [
    "ASLR",
    "re-randomization"
  ] 
}
```
