#!/usr/bin/env python3

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
sorted_words = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if lst.count(word) == 0:
            lst.append(word)
lst.sort()
print(lst)
