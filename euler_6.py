#!/usr/bin/env python
# encoding: utf-8
"""
euler_6.py
"""

import sys
import getopt


sum_of_squares = 0
sum = 0
for i in range(101):
  sum_of_squares += i**2
  sum += i

print sum_of_squares - sum**2
