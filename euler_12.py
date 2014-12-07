#!/usr/bin/env python
# encoding: utf-8
"""
euler_11.py
Last Modified: Sat Nov 22, 2014  10:15PM
"""
import numpy as np
import operator


triangle_number = 1
triangle = 1
while True:
    triangle  +=  triangle_number
    factor_count = 0
    for i in xrange(1, triangle / 2):
        if triangle % i == 0: factor_count += 1
    print triangle, factor_count
    if factor_count*2 == 500:
        print triangle_candidate
        break
    triangle_number += 1

