#!/usr/bin/env python3

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line[:5] == 'From ':
        words = line.split()
        if len(words) < 2: continue
        print(words[1])
        count+=1

print("There were", count, "lines in the file with From as the first word")
