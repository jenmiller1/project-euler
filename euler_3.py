#!/usr/bin/env python
# encoding: utf-8
"""
euler_3.py

"""

import sys
import getopt
import math


def factor(n):
  a = math.ceil(math.sqrt(n))
  b2 = a**2 - n
  while not math.sqrt(b2).is_integer():
    a += 1
    b2 = a*a - n
  return [a + math.sqrt(b2), a - math.sqrt(b2)]

def recursively_factor(n):
   smaller_factors = factor(n)
   print n, smaller_factors
   if not smaller_factors == [n, 1]:
     return  [recursively_factor(smaller_factors[0]), recursively_factor(smaller_factors[1])]
   else:
     return smaller_factors

n = 600851475143
print recursively_factor(n)
