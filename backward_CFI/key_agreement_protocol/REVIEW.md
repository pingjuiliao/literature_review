# A Novel Key Agreement Protocol Based on RET Gadget Chains for Preventing Reused Code Attacks

- Problem: Attackers exploit vulnerabilities to change RET gadget chains and control the order of program execution, threatening the security of software implementations. The previous key agreement protocols have not considered the security of protocol implementations at the source code level.
- Method: propose to decide the security of a protocol from its program execution and exploit RET gadget chains to improve present key agreement protocols. The
new key agreement protocol in this paper is secure in the implementations at the source code level.
- Design: The key agreement protocol introduces a trusted third-party to authenticate the chain of return addresses.
  - After reading the whole paper, I am still not sure how they generate the chain of return addresses.
- Result: Compared against other key agreement protocols such as MTI, MQV, and HMQV, it is secure against not only the man-in-the-middle attack but also the code reuse attack.
- Future Work: 
  - Return address chain could be dynamically generate. Therefore, a thrid-party verification could slow down the application due to inability to verify in time.
  - Other attack venues are still possible such as attackers on code pointers.

### flags
```
{
  "conference": "IEEE Access",
  "year": "2018",
  "keywords": [
    "Key Agreement Protocal",
    "Backward-edge CFI"
  ]
}
```
