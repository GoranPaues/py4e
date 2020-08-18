#!/usr/bin/env python3

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':') + 5
number = float(text[pos:])
print(number)