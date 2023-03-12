# 
- Problem: Embedded systems have become prominent targets for cyberattacks. To exploit firmware’s memory corruption vulnerabilities, cybercriminals harvest reusable code gadgets from the large shared library codebase (e.g., uClibc). Unfortunately, unlike their desktop counterparts, embedded systems lack essential computing resources to enforce security hardening techniques. Recently, we have witnessed a surge of software debloating as a new defense mechanism against code-reuse attacks; it erases unused code to significantly diminish the possibilities of constructing reusable gadgets. Because of the single firmware image update style, static library debloating shows promise to fortify embedded systems without compromising performance and forward compatibility. However, static library debloating on stripped binaries (e.g., firmware’s shared libraries) is still an enormous challenge.
- Method: 
  - The work shows that the challenge of static library debloating is not surmountable for MIPS firmware.
  - 
- Design: 
  - Why it works on MIPS?
    - The recent study on ARM disassembly tools has demonstrated that two complex problems, which are inline data in code sections and a mixture of ARM, 16-bit Thumb-1, and 32-bit Thumb-2 instruction sets, bring serious challenges to disassembling stripped ARM binaries [47]. In contrast, MIPS binaries do not have such complicated properties, making reliably disassembling MIPS binaries a solved problem.
    - Furthermore, MIPS Application Binary Interface (ABI) [79] specifications provide handy hints to optimize the address-taken blocks/functions detection. For example, a shared library is positionindependent code (PIC), in which most control flow targets are accessed or calculated through the global offset table (GOT).
  - Our contribution lies in how to identify unused library code without resolving indirect control flow targets.
    - MIPS uses GOT for all the uses of the libraries, which is easier
  - The core of our address-taken blocks/functions detection is to analyze the address loading patterns of the GOT and decide all legitimate addresses that could be referenced.
    - The only exception we observed is using function pointers as read-only global variables; their relocated addresses are stored in the .data.rel section. We handle this corner case with a special treatment.
  - building library dependency graph:
    - collecting functions needed by the firmware application:
      - First, we analyze the application binary’s import table to obtain imported APIs, which are explicitly invoked by the application. Instead of visiting the import table, a program may also manually load APIs via dlopen() and dlsym().
      - Second, we also include initialization and cleanup routines needed by shared libraries themselves (e.g., .init, .init_array, and .fini)
    - As a library’s function may also call the APIs defined in other libraries, given the APIs required by firmware, we need to keep all functions invoked in the library call chain in topological order so that we can decide which to debloat earlier.
- Result:  𝜇Trimmer to debloat shared libraries for SPEC CPU2017 benchmarks, popular firmware applications (e.g., Apache, BusyBox, and OpenSSL), and a real-world wireless router firmware image. Our experiments show that not only does 𝜇Trimmer deliver functional programs, but also it can cut the exposed code surface and eliminate various reusable code gadgets remarkably.
  - uTrimmer's library code reduction ratio for SPEC CPU2017 and firmware applications is 66.9% and 55.1%, respectively.
  - 𝜇Trimmer’s end-to-end running time, which varies from 1.1 hours to 6.2 hours. Symbolic execution is a well-known performance bottleneck, and the total running time is positively correlated with the number of libraries.
- Future Work:
  - Perform the same trimming on ARM architecture.
    - Need to handle the aforemention problems in ARM

### flags
```
{
  "conference": "ASPLOS",
  "year": "2022",
  "keyword": [
    "IoT",
    "Debloating",
    "Program Analysis"
  ]
}
```
