#!/usr/bin/env python3

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

number_of_spam_confidence = 0
total_spam_value = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        total_spam_value += float(line[line.find(':')+1:].strip())
        number_of_spam_confidence += 1

if number_of_spam_confidence > 0:
    avg_spam_confidence = total_spam_value / number_of_spam_confidence
    print('Average spam confidence:',avg_spam_confidence)
