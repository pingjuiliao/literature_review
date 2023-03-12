# Sponge-Based Control-Flow Protection for IoT Devices
- Problem: Code reuse attack, code injection, and fault attacks are  
- Method: SCFP encrypts and authenticates software with instruction-level granularity. During execution, an SCFP hardware extension between the CPU’s fetch and decode stage continuously decrypts and authenticates instructions.
- Design:
  - The idea behind SCFP is to encrypt programs at compile time using a sponge-based AE cipher.
    - indirect call site and return cite are patched with instructions so that 
  - Decryption is then performed within the CPU, instruction by instruction, just in time for execution.
  - The sponge-based AE cipher uses an internal state z , which provides the foundation for the CFI protection in SCFP.
- Limitation:
  - Indirect calls/jumps are hard to pre-determine at compile time. So, this work over-approximates the possible branches.
- Result: The work is secure against code reuse attack and fault attack. On the C benchmark-several programs in PULPino, SCFP incurs 19.8% and 9.1% on code size overhead and performance overhead respectively.
- Future work: 

### flags
```
{
  "conference": "Euro S&P",
  "year": "2018",
  "keywords": {
    "IoT",
    "Forward-edge CFI",
    "CFI",
    "Backward-edge CFI",
    "Fault Attack"
  }
}
```
