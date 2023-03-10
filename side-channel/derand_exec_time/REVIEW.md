# De-randomizing the Code Segment with Timing Function Attack

- Problem: Many effective defensive methods (e.g. ASLR, execute-only-memory) have been proposed to defeat the code reuse attack in the software system
- Method: this paper identifies a new weak point in these approaches, i.e., missing time protection. We propose a new attack method called timing function attack, which can initiate a code reuse attack even against the state-of-the-art defense techniques.
- Design: 
  - First, we collects code pointer in the code pointer table (such as GOT).
  - Then, we use function execution time to estimate what function it is. This technique can only be used under the follow constraints.
- Result: 
  - The time-channel attack can bypass XoM and function-level ASLR. 
  - They have evaluated their attack on ChakaraCore and ChromeV8.
  - The time difference for usable libc functions range from 2ms to 8ms.
- Future Work:
  - 


### flags
```
{
  "conference": "TrustCom",
  "year": "2020",
  "keywords": [
    "Side-channel",
    "ASLR"
  ]
}
```
