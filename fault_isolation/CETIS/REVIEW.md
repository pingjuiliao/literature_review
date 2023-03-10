# CETIS: Retrofitting Intel CET for Generic and Efficient Intra-process Memory Isolation
- Problem: existing intra-process memory isolation mechanisms suffers from high performance overhead, which makes promising protection policy impractical.
- Method: a framework that extends Intel CET for memory isolation scheme to make CPI, CFIXX, and JIT compilers practical.
- Result: lossless compression method of CPI incurs 4.05% and 3.97% overhead on SPEC 2006 and SPEC 2017 respectively. Overall, it's a better isolation scheme than Intel MPK.
- Future work:
  - Integrate with more work other than CPI.


### flags
```
{
  "conference": "ACM CCS",
  "year": "2022",
  "keywords": [
    "Fault Isolation",
    "Sandbox",
    "CFI",
    "Intel CET"
  ],
  "Related": [
    "CPI",
    "CFIXX"
  ]
}
```
