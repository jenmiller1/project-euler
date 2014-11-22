#!/usr/bin/env python
# encoding: utf-8
"""
euler_4.py
"""

import sys
import getopt

palindromes = []
for a in range(999, 111, -1):
 for b in range(999, 111, -1):
   product = a*b
   if str(product) == str(product)[::-1]:
     palindromes.append(product)

palindromes.sort()
print palindromes

