# Enforcing Forward-Edge Control-Flow Integrity in GCC & LLVM

- Problem: to date, CFI implementations have been research prototypes, based on impractical assumptions, ad hoc, heuristic techniques.
  - incremental compilation and dynamic libraries have remained privmary challenges for CFI implementations.
- Method: the work presents three compiler-based mechanisms that can be integrated into production compilers and be compatible with software-engineering apsect.
  - Virtual-table Verification(**VTV**): a CFI transformation implementation to protect C++ vtable specifically.
  - Indirect Function-Call Checks(**IFCC**): a CFI transformation implementation to protect all indirect calls.
  - Indriect-Call-Check Analysis (**FSan**): an optional indirect call checker that is designed to be used by developers to idnetify CFI violations that may lead to security issue.
  - such CFI implementations (VTV, IFCC) are pratical, highly efficient, and can be fully integrated into compiler without restrictions or simplifying assumptions.
- Design:
  - Virutal-table Verification(**VTV**)
    - VTV vcerifies that the vtable poointer about to be used in correct for the callsite. i.e. that it points either tto the vtable for the static type of the object or to a vtable for one of its descendent class.
    - VTV creates a special set of variables called **vtable-map variables**, one for each polymorphic class.
      - At runtime, a vtable-map variable will point to the set of valid vtable pointers for its associated class.
      - because the vtable-pointer sets need to be built before any virtual calls execute, VTV creates special constructor init functions, which run before standard initialization function, which run before <em>main</em>, ensuring the data is in place before any virtual calls are made.
    - vtable-map variabddles and vtable-pointer sets need to be read only to avoid introducing new vectors for attacks, but it requires some dynaic update whenever they are first initialized and dynamic library is loaded.
      - before updating its data, VTV finds all memory pages that contain vtable-map variables and btable-pointer sets and make them writable.
      - after it finishes the update it finds all the approriate pages and make them read-only
      - this requires VTV to find all the data quickly
        - to keep track of the vtable-pointer sets, the work wrote its own memory allocation scheme based on <em>mmap</em>.
        - to find vtable-map variables, VTV writes them into a specialed named section in the executable, which is page-aligned to help mmap quickly.
  - Indirect Function-Call Checks(**IFCC**)
    - IFCC protrects indirect calls by generateing jump tables for indirect-call targets and adding code at indirect-call sites to transform function pointers.
    - IFCC collects function-pointers into jump tables based on function-pointer sets with one table per set, like VTV.
    - indirect calls are replaced with a sequence of instructoins that use a mask and a base address to check the function pointer against the function-pointer set corresponding to the call site.
- Result:
  - A security analysis are made on compiling Chromium with CFI enforcement mechanism.
    - VTV achieves forward Average Indirect-target reduction(fAIR) at 95.2%, 6855 out of 142778 are unprotected.
    - IFCC achieves fAIR: 99.5, 908 out of 195338 are unprotected.
      - precisely, of the 908 unprotected instructions, 512 corresponds to the special functions created for function pointers returned from non-instrumented function; discounting those gives a fAIR vaalue 99.8%.
  - VTV performance: this performance measurement runs SPEC CPU 2006 C++ benchmarks with and without VTV to get a baseline.
    - VTV incurs overhead for omnetpp, astar, and xalancbmk ranges from 8 to 22%, while other benchmarks causes near-zero slowdown.
    - a closer looks shows that the near-zero overheads are because they do not perform enough calls per second.
    - replacing VTV with empty call stubs incurs overhead that ranges from 1.0 to 4.7, which yields the best case for any CFI enforcement can do.
  - IFCC performance: this work ran SPEC CPU 2006 C++ benchmark and Dromaeo benchmark, where the baseline is LLVM LTO.
    - IFCC incurs about 4% overhead in dromaeo and incurs about 6% in SPEC CPU 2006 C++ benchmark xalancbmk.
- Takeaway:
  - **IFCC**
    - each indirect call site is associated with its own jump table region (more like **trampoline region**), which consists of either legal jump instruction or trap instructions.
      - if all tables are page-aligned, a bitmask and a base pointer assignment are sufficed.
        - unfortunately, the ELF format supports arhitrary alignment but linux kernel does not (as of version 3.2.5 under ALSR with PIE).
      - if not, additional <em>sub(subtract)</em> should be introduced to compute the difference between base adress and the function pointer.
        - the paper does not develop paragraph for this specific method.
      - implication: the bitmask serve as a index transformation for the function pointer and the base pointer is the jump/trampoline region base address.
    - IFCC allows some false positives due to external code: 
      - any function that was not defined or declared during link-time optimizatioon will trigger a CFI violation. This can happen because:
        - JIT code
        - some exterenal functions can return external function pointers. e.g. <em>dlsym</em>, <em>sigaction</em>
        - some functions can be passed to external libraries and can be called there with external function pointers.
      - A flexible version of IFCC uses customed
        - "Insteead fo dfunctions being forced into the appropriate jump table, they are checked using the smae code sequences as VTV"
        - "This version of IFCC addes a comparison, a jump and function call to the inserted instruction sequence"
        - I assume that an additional check is made before referring its jump table.
      
### flags
```
{
  "conference": "USENIX",
  "year": 2014,
  "team": [
    "google",
    "Johns Hopkins"
  ],
  "keywords": [
    "forward-CFI",
    "LTO"
  ]
}
```
