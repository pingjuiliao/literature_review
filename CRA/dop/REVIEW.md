# Data-Oriented Programming: On the Expressiveness of Non-Control Data Attacks

- Problem: As control-flow hijacking defenses gain adoption, it is important ot understand the remaining capabilities of adversaries via memory exploit. The paper asks the question: whta is the real expressiveness power of non-control data attacks.
- Method: Data-oriented programming: by finding short sequentces of instructions in the program's control-abiding execution that enable specific operations simulating a Turing machine. Then, we find gadget dispatchers whcih are fragments of logic that chain together disjoont gadgets in an arbitrary sequence. Such expressive attacks allow the remote adversar6 to force the program to do its bidding.
- Result:
  - RQ1: how often do DOP gadget and DOP dispatcher exists in normal program?
    - This paper selects 9 software (bitconind, musl, busybox, wireshark, nginx, mcrypt, sshd, ProFTPD, WU-FTPD).
    - A total of 7518 gadgets and 5052 gadget dispatcher are identified from the 9 selected program.
    - For each application, the paper select one CVE and analyze the execution reachability from memory erros. 4 out of 9 progmras have at least one dispatcher reachable from the selected CVE.
  - RQ2: Can attacker build turing complete attacks with this method?
    - In the example of ProFTPD and Wireshark, they can locate turing-complete gadgets and dispatcher.
    - The paper shows that they can bypass some defenses via DOP, specifically, 
      - they bypassed ASLR leaked the private key from the OpenSSL in the ProFTPD server, the setting also bypass TASR and CCFI.
      - One consequence of reich expressivenesxs in DOP explotis is that a vulnerable program can simulate a remotely-controlled network bot.
      - DOP seuccsfully built a second-stage exploit for dlopen that permits arbitrary memory corruption or leakage of attacker intended locations.
  - RQ3: What is the security implication of this attack method?
    - We demonstrate three end-to-end case-studies which use DOP to exploit the program while bypassing ASLR and DEP to highlight the utility of Turing-completeness.
- Future Work:
  - ensures memory safety so that data pointer cannot be exploited.
  - Fault isolation can be used to protect all pointers but the overhead is presumably high.


### flags 
```
{
  "conference": "IEEE S&P",
  "year": "2016",
  "keywords": [
    "CRA",
    "CFI"
  ]
}
```
