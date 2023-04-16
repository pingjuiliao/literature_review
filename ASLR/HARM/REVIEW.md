# HARM: Hardware-assisted continuous re-randomization for microcontrollers
- Problem: Code reuse attacks are particularly noteworthy since the memory address of firmware code is static.
- Method: HARM periodically performs function-level address space layout re-randomization to mitigate the code reuse attack.
- Design:
  - HARM adpots function-level address space re-randomization to mitigate the code reuse attack.
  - HARM uses dynamically dispatched functions to .
  - HARM first perform off-device binary rewrite on the firmware image and then stores a read-only code flesh and metadata into the device for later address space layout re-randomization.
  - During runtime, the re-randomization engines rewrites the binary periodically.
  - The research group timed a JIT-ROP attack in a program that has overread vulnerability. The re-randomization time periods is set below the bar.
- Result: HARM has been observed a maximum overhead of 5.8% for CoreMark nenchmark when HARM performs a randomization every 200 ms, which is much shorter than the measured time needed by a real JIT-ROP like attack.
  - for BEEBS, it incurred 25% overhead in total:
  - the performance overhead majorly comes from re-randomize the jump table, :
- Future Work:
  - 5% is unbelievable for runtime rewrite every 200ms.
  - 

### flags
```
{
  "conference": "Euro S&P",
  "year": "2022",
  "keywords": [
    "IoT",
    "ASLR",
    "Re-randomization"
  ]
}
```
