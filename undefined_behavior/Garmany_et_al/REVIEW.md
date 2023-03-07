# Static Detection of Uninitialized Stack Variables in Binary Code

- Problem: memory corruption vulnerabilities utilizing stack anomalies are still prevalent while uninitialized variables plays an exceptional role due to their unpleasant property of unpredictability.
- Method: A statis interprocedural point-to analysis to detect all these bugs.
- Result: The analysis has found all uninitialized stack variables in Cyber Grand Challenges and 7 new bugs in binutils, but they are either patched or non-critical.
- Future Work:
  - Cleaning leftover on the stack could double the R/W operation. Therefore, I think a policy-based approach would be more practical.



### flags
```
{
  "conference": "ESORICS",
  "year": "2019",
  "keywords": [
    "Undefined Behavior"
  ]
}
```
