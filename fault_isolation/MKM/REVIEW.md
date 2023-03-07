# Mitigation of Kernel Memory Corruption Using Multiple Kernel Memory Mechanism

- Problem: kernel memory corruption can occur via the execution of malicious kernel code at the kernel layer.
- Method: separates kernel address space into two so that 
- Result: The evaluation results demonstrated that MKM can protect the kernel code and kernel data from a proof-of-concept kernel vulnerability that could lead to kernel memory corruption. In addition, the performance results of MKM indicate that the system call overhead latency ranges from 0.020 µs to 0.5445 µs, while the web application benchmark ranges from 196.27 µs to 6,685.73 µs for each download access of 100,000 Hypertext Transfer Protocol sessions. MKM attained a 97.65% system benchmark score and a 99.76% kernel compilation time.
- Future Work:
  - TODO


### flags
```
{
  "conference": "IEEE Access",
  "year": "2021",
  "keywords": [
    "Fault Isolation",
    "Kernel"
  ]
}
```
