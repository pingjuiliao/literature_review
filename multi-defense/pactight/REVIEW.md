# Tightly Seal Your Sensitive Pointers with PACTight

- Problem: Control-flow hijakcking attackes are critical. Though ARM introduces a new hardware security feature, Pointer Authentication, which ensures pointer integrity with cryptographic primitives, many PA-based mechanisms are still exposed to attacks.
- Method: PACTight provides a PA scheme that is composed of three security properties: unforgeability, non-copyabilitiy, and non-dangling. These properties are then used to construct a runtime library to enforce 4 desfenses policy, which are CFI, CPI, Return address Integrity, C++ VTable integrity
- Design: PACTight sign the sensitive pointers (code, heap objects) with (&p xor tag(p)), where tag(p) issues a random ID to the p.
  - for each heap object, generates its tag in the metadata region
  - for each pointers, (including pointers to heap objects), sign the (&p xor tag(p))
- Result: PACTight successfully defend against real world exploits and inxcur performance overhead of 4.07% even when enfoprcing the strongest defense, PACTight-CPI.
- Limitations: if not all the pointers are protected, the metadata region can be exploited with certain vulnerabilities.
- Future Work:
  - Paired PACTight with strong isolation mechanism, probably Intel MPK.


### flags
```
{
  "conference": "USENIX",
  "year": "2022",
  "keywords": [
    "ARM",
    "PAC",
    "Crypto",
    "CFI",
    "CPI"
  ]
}
```
