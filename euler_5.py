#!/usr/bin/env python
# encoding: utf-8
"""
euler_5.py
"""

import sys
import getopt

def calculate_multiple():
    i = 100
    while True:
        i += 10
        if i % 1000000 == 0:
            print i
        for divisor in range(3,21):
            if i % divisor != 0:
               break
            if divisor == 20:
                print 'GOT IT ', i
                return

calculate_multiple()
