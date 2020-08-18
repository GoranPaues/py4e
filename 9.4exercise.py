#!/usr/bin/env python3

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
emails = dict()
for line in fh:
    if line[:5] == 'From ':
        words = line.split()
        if len(words) < 2: continue
        emails[words[1]] = emails.get(words[1],0) + 1

bigEmail = None
bigCount = None
for email, count in emails.items():
    if bigCount is None or count > bigCount:
        bigEmail = email
        bigCount = count
print(bigEmail, bigCount)
