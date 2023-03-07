# A CFI Countermeasure Against GOT Overwrite Attacks

- Problem: Code reuse attack in GOT are left with RELRO. However, RELRO incurs high overhead.
- Method: A inter-module CFI scheme for GOT.
- Result: Full RELRO does take more times at startup. 
- Future Work:
  - One-time writable memory for GOT using Intel MPK
  - do the same thing in ARM

### flags
```
{
  "conference": "IEEE Access",
  "year": "2020",
  "keywords": [
    "Forward-edge CFI",
    "GOT",
    "CFI"
  ]
}
```
