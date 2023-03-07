# A CFI Countermeasure Against GOT Overwrite Attacks

- Problem: Code reuse attack in GOT are left with RELRO. However, RELRO incurs high overhead.
- Method: A inter-module CFI scheme for GOT.
- Result: Full RELRO does take more times at startup. 
- Future Work:
  - One-time writable memory for GOT using Intel MPK
  - do the same thing in ARM

# HCFI: Hardware-enforced Control-Flow Integrity

- Problem: Enabling CFI in real systems is not straritforward because CFG can only be approximated. Moreover, protecting backward-edge CFI without a shadow stack is questionable.
- Method: A full-featured CFI-enabled ISA in SparcV8.
- Result: HCFI incurred less than 1% performance overhead. As for security, the granularity of the forward-edge protection is directly proportional to the depth of the analysis performed on compile time.
- Future Work:
  - Portability to other architecture
    - Intel: We have Intel CET now
    - ARM: This could be an opportunity to find similar instruction to perform the aforementioned set.

# Silhouette: Efficient Proteceted Shadow Stacks for Embedded Systems

- Problem: control-flow hijacking remains a prevalent threat in embedded systmes due to resource and execution-tie constraints.
- Method:
  - enforced a coarse-grained CFI along with a parallel shadow stack.
  - modify all regular "store" instructions to "unprivileged store" instructions, except for the ones used for the shadow stack.
  - adopted a code scanner for other privileged instructions.
  - devised Sihouette-Invert at the cost of minor hardware change.
- Result: Silhouette incutrs a geometric mean of 1.3% and 3.4% performance overhead, and a geometric mean of 8.9 and 2.3% code size overhead on the CoreMark-Pro qand BEEBs benchmark suites, resepctively.
- Future Work:
  - Memory-efficient shadow stack for embedded systems
  - Extend the unprivileged move to more powerful protection mechanism such as CPI.

# Zipper Stack: Shadow Stacks Without Shadow

- Problem: Existing return address protecting mechanisms only work with limited threat models, which assume attacker cannot break the isolation mechanism.
- Method: This presents a hardware implementation of chained MAC authentication for return address.
- Challenge:
  - Cryptography-based pointer protection are vulnerable to replay attacks since attacker can simply copy the value of the .
- Result: The scheme can protect return addresses 
secure against replay attack and rare collision against brute force attack, incur 2% overhead in RISC-V implementation, (but 20% in LLVM implementation)
- Future Work:
  - The scheme requires a top register to store the latest return address.
  - problem: prevent one gadget, the entropy of one gadget attack is still low


# SoK: Shining Light on Shadow Stack

- Problem: Control-flow backward edges are protected by stack canary in practice. Shadow stack, while secure, are rarely deployed due to performance and compatibility issues.
- Method: A comprehensive analysis of all possible shadow stack mechanisms in security, compatibility, and performance.
- Design:
  - They recommend compacted register-offsetted shadow stack for performance and compatibility.
  - Neither MPK nor MPX overhead are acceptable; therefore, information hiding are more practical to deploy.
  - For hardware manufacturer, they recommend devising a privileged move instruction for hardware support for shadow stack scheme.
- Result: The compacted register-offsetted shadow stack is compatible with threading and unprotected code. It incurs 5% performance overhead in SPEC 2006.
- Future Work:
  - other secure isolation scheme than information hiding
  - hardware shadow stack such as Intel CET

# MARDU: Efficient and Scalable Code Re-randomization

- Problem: While code reuse attacks evolves in complexity, defenses designs are neither practical nor scalable.
- Method: a system-wide re-randomization-on-crash mechanism to provide a scalable scheme to prevent attackers from harvesting code reuse gadget, which supports code sharing for compatibility.
- Challenge: 
  - having fine-grained ASLR with re-randomization while not sacrificing performance.
- Design:
  - MARDU fine-grained the randomization in function level.
  - MARDU application must go through a trampolines region to enter into or return from a function. The trampoline mechanism exists for several reasons:
    - First, it requires no runtime tracking for rerandomization.
    - Second, it hides the code pointer in the real code region. (but the trampoline addresses are exposed) 
    - Third, since trampoline and code regions are seperated, XoM can be enable for the code region.
    - return address (code pointers to the trampoline region) can still be enabled.
  - One process, instead of per-process, is dedicated to preform re-randomization for the entire system.
  - MARDU only performs re-randomization while detect malicious behavior on crash, flushing attackers knowledge while attackers cannot trigger a crash.
  - MARDU modified kernel to manage code cache for randomized code so that the code can be shared.
- Result: MARDU incurs 5.5% and 4.4% performance overhead in SPEC 2006 and nginx respectively, confirming practicality and scalability.
- Future work:
  - Since the trampoline addresses are stationary, the full function reuse can be a good attack surface. 
    - CFI to prevent the full function reuse of MARDU application. 
    - perform static analysis that prevents the linked modules from doing malicious things.
  - side-channel attack via hardware.



# HARM: Hardware-assisted continuous re-randomization for microcontrollers
- Problem: Code reuse attacks are particularly noteworthy since the memory address of firmware
code is static.
- Method: HARM periodically performs function-level address space layout re-randomization to mitigate the code reuse attack.
- Design:
  - HARM adpots function-level address space re-randomization to mitigate the code reuse attack.
  - HARM uses indirect jumps instead of expensive runtime tracking.
  - HARM first perform off-device binary rewrite on the firmware image and then stores a read-only code flesh and metadata into the device for later address space layout re-randomization.
  - During runtime, the re-randomization engines rewrites the binary periodically.
  - The research group timed a JIT-ROP attack in a program that has overread vulnerability. The re-randomization time periods is set below the bar.
- Result: HARM has been observed a maximum overhead of
5.8%  when HARM performs a randomization every 200 ms, which is much shorter than the measured time needed by a real JIT-ROP like attack.
- Future Work:
  - 5% is unbelievable for runtime rewrite every 200ms.


- Problem: porting ASLR to resource-constrained IoT devices is challenging due to limited memory space.
- Method: A trusted runtime randomization engine that validate the entry point of functions and generates the given function body on the randomized region.
- Design:
  - A non-executable application code copy is placed on the unpriviledged address space.
  - Execution on the non-executable leads to hardware fault and the hardware fault trigger the randomization engine to generaete executable code in randomized address. Note that they perform randomization for each function exactly once. There is no re-randomization
  - It is difficult for fASLR to handle indirect call, so the application should be compiled without using indirect addressing.
  - fASLR does not re-randomize the called function address. Instead, they rewrite the call instruction to perform 
  - The randomization engine is trusted and protected via the Trustzone-M
  - fASLR also apply a function desposal mechanism to remove functions that should not be executed anymore from the address space.
- Result: fASLR achieves a high randomization entropy and incurs a runtime overhead of less than 10%. Furthermore, it achieves 5% code size overhead.
- Future Work:
  - The trampoline method can incur less performance and memory overhead. On top of it, we can make it a rerandomization technique.
  - The authenticated Call Stack mechanism can be used if the performance is acceptable.
  


# Randezvous: Makeing Randomization Effective on MCUs

- Problem: MCU software is typically written in C and is prone to memory safety vulnerabilities that are exploitable by remote attackers to launch code reuse attacks and code/control data leakage attacks.
- Method: atop code layout randomization, it 
- Design:
  - Randezvous, at compile time, randomizes the layout of each function and then, within each function, randomize the layout of each basic blocks. Inbetween codes, trap instruction are injected to create different offset.
  - Unused data memory are filled with decoy pointer, which points to the injected trap instruction.
  - Randezvous deploy RA-style(no compare) shadow stack mechanism and it is placed within the data region so that it is also camouflaged by the decoy pointer. It also uses pseudo random generation to dynamically take random strides for each pushes of return addreess.
  - Randezvous promotes local variables to global variables, especially code pointers, so that these variables can be protected by the data region filled with decoy pointers.
  - Randezvous further overwrites stale return address on shadow stack with null bytes to prevent leaking overread. (so that an attacker can only leak return addresses that are on the call stack, excluding the latest one on the Link Register.)
  - To defend against brute force attack, Randezvous artificially delay a reboot whenever it detects a trap made by Randezvous policy violation. In this way, attackers' failed attempt would take longer time.
  - To prevent spraying attack that filling data region with the same gadget, they introduce global guard, a stack canary that prevents data overwrite, which also establish entropy
- Result: Randezvous is secure against return-to-libc attack for three days. Randezvous’s overhead is evaluated on three benchmark suites and two real-world applications.
average, Randezvous incurred 5.9% performance overhead, 15.4% code size overhead, and 22.0% data size overhead.
- Future Work:
  - Some observation let me think a policy-based defense methods are probably better.
    - because Randezvous has low entropy on small devices, which is vulnerable to brute-force attack.
    - the defense mechanism kind of mixed up to frustrate attackers but not complete secure.
    - Information leak could be possible in many ways:
      - arbitrary read twice to probe what have chaneged

# CETIS: Retrofitting Intel CET for Generic and Efficient Intra-process Memory Isolation
- Problem: existing intra-process memory isolation mechanisms suffers from high performance overhead, which makes promising protection policy impractical.
- Method: a framework that extends Intel CET for memory isolation scheme to make CPI, CFIXX, and JIT compilers practical.
- Result: lossless compression method of CPI incurs 4.05% and 3.97% overhead on SPEC 2006 and SPEC 2017 respectively. Overall, it's a better isolation scheme than Intel MPK.
- Future work:
  - Integrate with more work.


# You Shall Not (by)Pass! Practical, Secure, and Fast PKU-based Sandboxing

- Problem: existing PKU-based isolation approches are not complete.
- Method: a PKU-based sandboxing framework to overcome limitations of existing approaches.
  - conclusively handle unsafe instructions
  - Full PKU-pitfall protection except for Signal context attacks.
- Result: comeplete handle of unsafe instructions and PKU pitfalls protections while requires minor kernel change.
- Future Work:


# Static Detection of Uninitialized Stack Variables in Binary Code

- Problem: memory corruption vulnerabilities utilizing stack anomalies are still prevalent while uninitialized variables plays an exceptional role due to their unpleasant property of unpredictability.
- Method: A statis interprocedural point-to analysis to detect all these bugs.
- Result: The analysis has found all uninitialized stack variables in Cyber Grand Challenges and 7 new bugs in binutils, but they are either patched or non-critical.
- Future Work:
  - Cleaning leftover on the stack could double the R/W operation. Therefore, I think a policy-based approach would be more practical.



