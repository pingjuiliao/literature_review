#!/usr/bin/env python3
import argparse
import datetime
import json
import os

PWD = "."
MARKDOWN_FILENAME="REVIEW.md"
FLAG = b"### flags"
FLAG_SEC = b"### flags"
WRITE_TO="./RESULT.md"

def is_queried(filepath, query):
    DELIM = b"\#"
    with open(filepath, "rb") as f:
        s = f.read()
        flags = s[s.find(FLAG)+len(FLAG):].split(DELIM)
        f.close()

    for flag in flags:
        flag = flag.strip()
        if flag in query:
            return True
    return False

def is_queried2(filepath, query):
    json_txt = None
    with open(filepath, "rb") as f:
        b_str = f.read()
        flag_section = b_str[b_str.find(FLAG_SEC):]
        flag_sec_splt = flag_section.split(b"```")
        if len(flag_sec_splt) == 3:
            json_txt = flag_sec_splt[1]
        else:
            # DEBUG
            print(filepath, len(flag_sec_splt))
        f.close()
    if json_txt is None:
        return False
    try:
        js = json.loads(json_txt.decode())
    except:
        print("file {} failed in JS format".format(filepath))
        quit()
    print(js)
    return True

def write_to_result(filepath):
    print("writing", filepath)
    with open(filepath, "rb") as f:
        b_str = f.read()
        b_str = b_str[:b_str.find(FLAG)]
        f.close()

    with open(WRITE_TO, "ab") as f:
        f.write(b_str)
        f.close()

def parse_markdown(query=set()):
    for root, dirs, files in os.walk(PWD):
        for file in files:
            if file != MARKDOWN_FILENAME:
                continue
            file_abspath = os.path.join(root, file)
            if is_queried2(file_abspath, query):
                write_to_result(file_abspath)

def form_query():
    # Prepare for parsing time argument
    now = datetime.datetime.now()
    this_year = int(now.strftime("%Y"))

    # Prepare for parsing time argument


    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keyword", action="store")
    parser.add_argument("-af", "--after", action="store", type=int, default=1993)
    parser.add_argument("-b4", "--before", action="store", type=int, default=this_year)
    conference_group = parser.add_mutually_exclusive_group()
    conference_group.add_argument("--top", action="store_true")
    conference_group.add_argument("--journal", action="store_true")

    args = parser.parse_args()

    # Handle time
    print("Querying from {} to {}......".format(args.after, args.before))
    query = set([year for year in range(args.after, args.before+1)])

    # Handle topics

    # Handle conference
    if args.top:
        query = query.union(["IEEE S&P", "USENIX", "NDSS", "ACM CCS"])
    elif args.journal:
        query = query.union(["IEEE Access", "IEEE IoT Journal"])

    return query

def main():
    query = form_query()
    print(query)
    if query and os.path.exists(WRITE_TO):
        os.unlink(WRITE_TO)
    parse_markdown(query)


if __name__ == '__main__':
    main()
