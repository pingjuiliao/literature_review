# HCFI: Hardware-enforced Control-Flow Integrity

- Problem: Enabling CFI in real systems is not straritforward because CFG can only be approximated. Moreover, protecting backward-edge CFI without a shadow stack is questionable.
- Method: A full-featured CFI-enabled ISA in SparcV8.
- Result: HCFI incurred less than 1% performance overhead. As for security, the granularity of the forward-edge protection is directly proportional to the depth of the analysis performed on compile time.
- Future Work:
  - Portability to other architecture
    - Intel: We have Intel CET now
    - ARM: This could be an opportunity to find similar instruction to perform the aforementioned set.

### flags
```
{
  "conference": "ACM CODASPY",
  "year": "2016",
  "keywords": [
    "CFI",
    "Forward-edge CFI",
    "SparcV8"
  ]
}
```
\#ACM CODASPY
\#2016
\#CFI
\#Forward-edge CFI
\#SparcV8
