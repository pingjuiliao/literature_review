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

### flags
```
{
  "conference": "ACSAC",
  "year": "2022",
  "keywords": [
    "IoT",
    "ASLR",
    "Fine-grain ASLR",
    "Shadow Stack"
  ],
  "complementary": [
    "XoM",
    "Stack Canary"
  ]
}
```
