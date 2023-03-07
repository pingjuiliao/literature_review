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


### flags
```
{
  "conference": "ESORICS",
  "year": "2020",
  "keywords": [
    "Shadow Stack",
    "Crypto",
    "Backward-edge CFI"
  ]
}
```

\#ESORICS
\#2020
\#Shadow Stack
\#Cryptography
\#Backward-edge CFI

