# Control-Flow Bending: On the Effectiveness of Control-Flow Integrity

- Problem: While recent research has shown that coarse-grained CFI does not stop attacks, fine-grained CFI is believed to be secure. This work argues that assessing the effectiveness of practical CFI implementations is non-trivial and that common evaluation metrics fail to do so.
- Method: Using a generalization of non-control-data attacks which we call Control-Flow Bending (CFB), we show how an attacker can leverage a memory corruption vulnerability to achieve Turing-complete computation on memory using just calls to the standard library.
- Design:
  - Control-flow Bending (CFB): by controlling the critical non-control data(e.g. function arguments), the control flow can be directed by users.
  - Evaluating coarse grain CFI
    - searching for gadgets that are right after the call instructions.
    - while 99% of the gadgets are removed from the binary, the security analysis shows that arbirary syscall can still occur.
  - Evaluating fully-precise CFI: 
    - fully-precise CFI: indirect branch target are confined to the precise set of possible target
    - evaluated on nginx, apache, smbclient, wireshark, xpdf and mysql.
    - dispatcher function: "write-what-where" style of functions can be 
    - loop inject: say a function is called twice in certain function, injecting return address to previous call site
    - therefore, this work argues that shadow stack (or similar mechanism) is necessary.
- Results:
  - Among nginx, apache, smbclient, wireshark, only nginx can survive against full exploit.
  - this work argues that shadow stack (or similar mechanism) is necessary.
- Future Work:
  - Evaluation of this work among IoT binaries.

### flags
```
{
  "conference": "USENIX",
  "year": "2022",
  "keywords": [
    "Code reuse attack",
    "CFI",
    "Forward-edge CFI"
  ]
}
```

