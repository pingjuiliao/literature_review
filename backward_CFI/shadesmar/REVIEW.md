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

### flags
```
{
  "conference": "IEEE S&P",
  "year": "2019",
  "keywords": [
    "Backward CFI",
    "Shadow Stack"
  ],
  "Related": [
    "Intel MPK",
    "Intel MPX"
  ]
}
```
