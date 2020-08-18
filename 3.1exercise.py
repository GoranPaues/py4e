#!/usr/bin/env python3

hrs = input("Enter Hours:")
hrs_number = float(hrs)
rate = input("Enter rate per hour:")
base_rate = float(rate)
extra_rate = 1.5*base_rate
if hrs_number <= 40:
    print(str(hrs_number*base_rate))
else:
    extra_hrs_number = hrs_number - 40
    print(str(extra_hrs_number*extra_rate + 40*base_rate))
