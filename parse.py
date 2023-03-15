#!/usr/bin/env python3
import argparse
import datetime
import json
import os

PWD = "."
MARKDOWN_FILENAME="REVIEW.md"
FLAG = b"### flags"
FLAG_SEC = b"### flags"
WRITE_TO="./SUMMARY.md"

written_count = 0

TOP_CONFERENCE = ["IEEE S&P", "ACM CCS", "USENIX", "NDSS"]
JOURNAL = ["IEEE Access", "IEEE IoT Journal"]

class Query:
    def __init__(self):
        now = datetime.datetime.now()
        this_year = int(now.strftime("%Y"))
        self.before = this_year
        self.after = 1993
        self.topics = set()
        self.conference = set()
        self.exclude_conf = set()

    def set_time(self, after, before):
        if after is not None:
            self.after = after
        if before is not None:
            self.before = before

    def add_keywords(self, keywords: list[str]):
        if keywords is None:
            return
        self.topics = self.topics.union(set(keywords))

    def add_conference(self, conf: list[str]):
        if conf is None:
            return
        self.conference = self.conference.union(set(conf))

    def exclude_conference(self, conf: list[str]):
        if conf is None:
            return
        self.exclude_conf = self.exclude_conf.union(set(conf))


def is_queried(filepath, query):
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

    if 'keywords' not in js or 'conference' not in js or 'year' not in js:
        print(filepath, "does not have correct JSON format")
        quit()

    if query.conference and js['conference'] not in query.conference:
        return False
    if js['conference'] in query.exclude_conf:
        return False
    published_year = int(js['year'])
    if published_year < query.after or query.before < published_year:
        return False
    if query.topics and not set(js["keywords"]).intersection(query.topics):
        return False

    return True

def write_to_result(filepath):
    global written_count
    print("writing...", filepath)
    with open(filepath, "rb") as f:
        content = f.read()
        content = content[:content.find(FLAG)]
        f.close()

    design_sec_idx = content.find(b"- Design:")
    if design_sec_idx >= 0:
        part_a = content[:design_sec_idx]
        part_b = content[content.find(b"- Result:"):]
        content = part_a + part_b

    with open(WRITE_TO, "ab") as f:
        f.write(content)
        f.close()
    written_count += 1

def parse_markdown(query):
    for root, dirs, files in os.walk(PWD):
        for file in files:
            if file != MARKDOWN_FILENAME:
                continue
            file_abspath = os.path.join(root, file)
            if is_queried(file_abspath, query):
                write_to_result(file_abspath)

def form_query():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keyword", nargs="+", action="store")
    parser.add_argument("-af", "--after", action="store", type=int)
    parser.add_argument("-b4", "--before", action="store", type=int)
    conference_group = parser.add_mutually_exclusive_group()
    conference_group.add_argument("--top", action="store_true")
    conference_group.add_argument("--sub", action="store_true")
    conference_group.add_argument("--journal", action="store_true")
    args = parser.parse_args()

    # Handle time
    query = Query()
    query.set_time(args.after, args.before)

    # Topics
    query.add_keywords(args.keyword)

    # Handle conference
    if args.top:
        query.add_conference(TOP_CONFERENCE)
    elif args.sub:
        query.exclude_conference(TOP_CONFERENCE)
    elif args.journal:
        query.add_conference(JOURNAL)
    return query

def main():
    query = form_query()
    if query and os.path.exists(WRITE_TO):
        os.unlink(WRITE_TO)
    parse_markdown(query)
    print("{} papers written".format(written_count))


if __name__ == '__main__':
    main()
