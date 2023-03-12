# HCIC: Hardware-Assisted Control-Flow Integrity Checking

- Problem: Code reuse attack emerges as a new class of security threat. However, software-based defense incurred too much overheads while hardware approaches may require extending ISAs. 
- Method: HCIC is a new hardware-assisted control flow checking method to resist CRAs with negligible performance overhead without extending ISAs, modifying the compiler or leaking the encryption/decryption key.
- Design: 
  - HCIC leverages Silicon Physical Unclonable Functions (PUF) to perform key generation and authentication, which requires no expensive hardware.
  - Before the code is loaded to the memory, the branch target "instruction" is encrypted(Hammer distant byte and XOR).
    - During runtime, every jump/call instruction encode(XOR) the target address so that the valid sites could only be those which is encoded.
    - note that these operation in HCIC's design happens in the hardware.
  - The call/return encryption scheme is Encrypted Hammering Distance
    - EHD = rotate_right(((HD(retaddr, key) << 24) & key >> 8), key & 0b11111)
    - EHD and the return address will be pushed onto the stack. On function return, EHD and the return address pair are checked.
    - HCIC further employ a counter protection on call/return so that the nth call/return will have different keys.
  - THe jump authentication scheme is performed by PUF.
  - They uses different scheme to prevent leaking key secret.
- Result: The SPEC CPU2006, BioBench, MiBench, and Stream benchmarks are used in HCIC experiment. Both the performance overhead and the binary size overhead are less than 1 %.
  -If the legal target addresses of some call or jmp instructions are not covered by the profiled CFG, HCIC would produce false positives when the program decrypts unencrypted instructions at those addresses.
- Future Work:
  - Attack on this method:
    - hijacking return address: we can change the EHD and return address pair to redirect control flow.
      - Since this is a hardware-based approach, we probably cannot deduce the EHD value via debugger.
      - Then, we can force the system to use the same key to infer the encoding algorithm and the key.
  - Other limited attackes:
    - Full function reuse is possible since they are valid jump/call target.
    - We can reuse any EHD and return address pair.
  - Encrypting the instruction that are in the set of the legal branch targets is interesting.
    - However, a loop might have to decrypt and then encrypt every time-> performance overhead

### flags
```
{
  "conference": "IEEE IoT Journal",
  "year": "2018",
  "keywords": [
    "IoT",
    "Forward-edge CFI",
    "Backward-edge CFI",
    "CFI",
    "PUF"
  ]
}
```
