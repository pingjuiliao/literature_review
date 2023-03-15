# 
- Problem: Shadow stacks play an important role in protecting return addresses to mitigate ROP attacks. Parallel shado stacks are known not to support multi-threading well. On the other hand, compact shadow stacks must maintain a separate shadow stack pointer in thread-local storage (TLS), which can be implemented in terms of a register or the perthread Thread-Control-Block (TCB), suffering from poor compatibility in the former or high performance overhead in the latter. In addition, shadow stacks are vulnerable to information disclosure attacks.
- Method: the paper present, BUSTK, a performant, comaptible shadow stack.
  - Bustk places a parallel shadow stack just below a thread’s call stack, avoiding the need to maintain a separate shadow stack pointer and making it now well-suited for multi-threading.
  - Bustk uses an efficient stack-based thread-local storage mechanism, denoted STK-TLS, to store thread-specific metadata in two TLS sections just below the shadow stack in dual redundancy (as each other’s buddies), so that both can be accessed and updated in a lightweight manner from the call stack pointer rsp alone.
  - Bustk re-randomizes continuously (on the order of milliseconds) the return addresses on the shadow stack by using a new microsecond-level runtime re-randomization technique
- Result: Bustk still has comparable performance overheads as Shadesmar.
- Future Work:

### flags
```
{
  "conference": "TOSEM",
  "year": "2022",
  "keywords": [
    "Shadow Stack",
    "Backward-edge CFI",
    "ASLR",
    "Re-randomization"
  ]
}
```
