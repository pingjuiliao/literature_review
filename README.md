# Literature review
My literature review of security paper, mostly defense mechanism against memory corruption.

## parse.py
The parser parse all the reviewed topics and organized them based on keywords, conferences, and published years. The result of the parser will be dumped into "./RESULT.md" here.

Usage: 
Search for specific topic
```
./parse.py --keyword "Shadow Stack" "CFI"
# or ./parse.py -k "Shadow Stack" "CFI"
```

Search for defined conference range
```
./parse.py --sub  # search for papers not in top conference
```

Search for the most recent papers
```
./parse.py --after 2020
```

We can also combine aforementioned query together
```
./parse.py --top --keyword "Fault Isolation" --after 2020
```

