# The Taming of the Stack: Isolating Stack Data from Memory Errors

- Problem: Historically, stack defenses focus on the protection of code pointers, such as return addresses, but emerging techniques to exploit memory errors motivate the need for practical solutions to protect stack data objects as well. However, recent approaches provide an incomplete view of security by not accounting for memory errors comprehensively and by limiting the set of objects that can be protected unnecessarily.
- Method: The paper presents DATAGUARD, a safe stack mechanism of which a more comprehensive and accurate safety analysis that proves a larger number of stack objects are safe from memory errors, while ensuring that no unsafe stack objects are mistakenly classified as safe.
- Result: 
  - DATAGUARD ensuring that no memory safety violations are possible for any stack objects classified as safe, removing 6.3% of the stack objects previously classified safe by the Safe Stack method.
  - DataGuard blocks exploit of all 118 stack vulnerabilities in the CGC Binaries.
  - DATAGUARD extends the scope of stack protection by validating as safe over 70% of the stack objects classified as unsafe by the Safe Stack method, leading to an average of 91.45% of all stack objects that can only be referenced safely.
  - DATAGUARD reduces the overhead of using Clang’s Safe Stack defense for protection of the SPEC CPU2006 benchmarks from 11.3% to 4.3%.
- Future Work:
  - If the so-called anaylsis is accurte, we can develop a analysis, probably a checker, to warn developer in the compiler level.
  - If a code pointer is unsafe, the safe stack provides little defense.
    - In this case, we should develop what is critical (the answer would be code pointer & something)
  - If the isolation scheme is not strong enough(e.g. IH), vulenrable variables can still corrupt the safe stack

### flags
```
{
  "conference": "NDSS",
  "year": "2022",
  "keywords": [
    "Safe Stack", 
    "Backward-edge CFI",
    "Program Analysis"
  ]
}
```
