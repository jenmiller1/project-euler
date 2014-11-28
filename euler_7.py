#!/usr/bin/env python
# encoding: utf-8
"""
euler_7.py

"""

import sys
import numpy as np
import math


def nth_prime(n):
  primes = [2]
  test_num = 3
  while(len(primes) < n):
    factor = primes[0]
    prime_count = 0
    test_num_limit = math.ceil(math.sqrt(test_num))
    limit_index = get_largest_prime_to_test(test_num_limit, primes)
    broken = False
    for factor in primes[:limit_index+1]:
      if test_num % factor == 0:
        broken = True;
        break
    if not broken and factor == primes[limit_index]:
      primes.append(test_num)
      print 'adding', test_num, len(primes)
    test_num += 2

def get_largest_prime_to_test(sqrt_limit, primes):

  limit_list = list((np.array(primes) < sqrt_limit))
  if limit_list.count(False) > 0:
    return limit_list.index(False)
  else:
    return len(limit_list)

nth_prime(10001)
