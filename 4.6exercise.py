#!/usr/bin/env python3

def computepay(h,r):
    extra_rate = 1.5*r
    if h <= 40:
        return (str(h*r))
    else:
        extra_h = h - 40
        return str(extra_h*extra_rate + 40*r)

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate per hour:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)