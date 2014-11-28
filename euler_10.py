#!/usr/bin/env python
# encoding: utf-8
"""
euler_10.py
"""

def primes_lt(n):
  primes = [2]
  numbers = range(n+2)
  next_prime = 2
  while True:
    print next_prime
    counter = next_prime + next_prime
    while counter <= n:
      numbers[counter] = -1
      counter += next_prime
    num = next_prime + 1
    while numbers[num] == -1 and num < n:
        num += 1
    if num < n:
      next_prime = num
      primes.append(next_prime)
    else:
      print 'DONE', sum(primes)
      return

primes_lt(2000000)





