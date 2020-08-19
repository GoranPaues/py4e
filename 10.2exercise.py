#!/usr/bin/env python3

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
hours = dict()
for line in fh:
    if line[:5] == 'From ':
        words = line.split()
        time = words[5].split(':')
        if len(words) < 2: continue
        hours[time[0]] = hours.get(time[0],0) + 1
sorted_hours = sorted([(hour,count) for hour,count in hours.items()])
for hour, count in sorted_hours:
    print(hour,count)
