# OPEC: Operation-based Security Isolation for Bare-metal Embedded Systems

- Problem: Previous research intends to enforce both privilege isolation and resource isolation for global variables and peripherals. However, it suffers from partition-time and execution-time over-privilege issues, due to the limited hardware resources (MPU regions) and the improper way to partition a program.
- Method: OPEC is e operation-based isolation for bare-metal embedded systems. 
  - An operation is a logically independent task composed of an entry function and all functions reachable from it.
  - To solve the partition-time overprivilege issue, we utilize the global variables shadowing technique to reduce the needed MPU regions to confine the access of the global variables.
  - To mitigate the executiontime over-privilege issue, we split programs into code compartments (called operation) that only contain necessary functions to perform specific tasks, thereby removing the resources needed by unnecessary functions
- Design:
  - Global variable shadowing: We make a shadow copy of each shared global variable of one operation and put it into a continuous memory space that is only accessible by that operation. By doing so, the continuous memory space only contains global data necessary for a specific operation, which avoids incorporating redundant resources. 
  - For the execution-time over-privilege issue, we mitigate it through an approach that one operation only includes the functions needed to perform a specific task. Indeed, a function may contain some basic blocks that are not executed at runtime, which could also cause the execution-time overprivilege issue.
  - Furthermore, our system virtualizes the MPU regions to use the MPU flexibly and facilitate the operation partitioning. Explicitly, our system supports reconfiguring the MPU on demand at runtime.
  - OPEC-workflow
    - Specifically, OPEC-Compiler gets the application source code and the operation entry function list specified by developers.
    - Then it performs a static analysis to identify the global data and peripherals needed by each operation to generate the operation policy.
    - After that, it uses the operation policy to produce the final program image. 
    - OPEC-Monitor is linked to the image during the compiling time to enforce the isolation policy. The operation switch is triggered by a software interrupt (the SVC instruction), which will be handled by OPEC-Monitor.
    - OPEC-Monitor first performs data synchronization based on the corresponding policy. Then, it enforces resource access permissions by setting up the MPU.
- Result: Our evaluation shows that OPEC can achieve the security guarantees for the privilege and resource isolation with negligible runtime overhead (average 0.23%), moderate Flash overhead (average 1.79%), and acceptable SRAM overhead (average 5.35%).
- Future Work:


### flags
```
{
  "conference": "EuroSys",
  "year": "2022",
  "keywords": [
    "Fault Isolation",
    "IoT" 
  ]
}
```
