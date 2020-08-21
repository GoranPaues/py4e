#!/usr/bin/env python3
import re

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_882207.txt"

fh = open(fname)
total_sum = 0
for line in fh:
    numbers = re.findall('[0-9]+',line)
    for number in numbers:
        total_sum += float(number)
print('Sum:',round(total_sum))