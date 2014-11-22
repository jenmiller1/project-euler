#!/usr/bin/env python
# encoding: utf-8
"""
euler_2.py

"""

import sys
import getopt


fib1 = 1
fib2 = 1
sum = 0
while fib2 < 4e6:
  if fib2 % 2 == 0:
    sum += fib2
  old2 = fib2
  fib2 = fib1 + fib2
  fib1 = old2

print sum
