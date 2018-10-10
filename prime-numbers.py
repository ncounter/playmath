#!/usr/bin/python

import sys, os, ConfigParser, datetime

def isDivisorOf(d, n):
   return n%d == 0

def isPrime(n):
   if n == 1:
      return True

   # highest divisor 'i' cannot be no greater than the half of the number 'n',
   # as 'n' would then be a multiple by 2 of 'i'
   for i in range(2, (n/2)+1) :
      if isDivisorOf(i, n):
         return False

   return True

def main():
   primes = []

   for n in range(1, 1000):
      if isPrime(n):
        primes.append(n)

   sys.stdout.write(str(len(primes)))
   sys.stdout.write('\n')

if __name__ == "__main__":
   main()
