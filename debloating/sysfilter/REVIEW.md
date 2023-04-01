# sysfilter: Automated System Call Filtering for Commodity Software

- Problem: OS kernels allows full and unrestricted use of the entire system call set. This not only violates the principle of least privilege, but also enables attackers to utilize extra OS services.
- Method: this work presents sysfilter, a binary analysis-based framework that automatically limites OS services and reduces the attack surface.
- Design:
  - The work conducts Call graph analysis to determine reachability of functions.
  - Then, they use classic live variable analysis to determine Syscall set.
  - Finally, they construct Seccomp-BPF allow list to sandbox the program.
- Result: They evaluate sysfilter in terms of correctness, runtime performance overhead, and effectiveness.
  - correctness: over 411 binaries, including GNU coreutils, Nginx, Redis, SPEC CINT2006, SQLite, FFmpeg, MariaDB, Vim, and so on. In all cases, sysfilter succesfully extract a complete and tight syscall set.
  - performance: in the case of SPEC, a run-time slowdown less than 1% under all conditions and search methods.
  - effectiveness: depending on the exact vulnerability, the percentage of binaries that can still attack the kernel ranges from 0.09% to 64.34%.
- Future Work:
  - we can further bound the principle of lesat privilege by reading the arguments of functions.
    - e.g. execve("/bin/ls", 0, 0) then execve can only incurred with these arguemnt.
    - this might needs some coarse grained CFI


### flags
```
{
  "conference": "RAID",
  "year": "2023",
  "keywords": [
    "Debloating",
    "Program Analysis",
    "Seccomp-BPF" 
  ]
}
```
