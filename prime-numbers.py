#!/usr/bin/python

import sys

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
   if len(sys.argv) < 2:
      sys.stdout.writelines('Argument missing: command format should look like the following\n' +
          '  "python prime-numbers.py limit<number>"\n')
      return

   primes = []

   limit = int(sys.argv[1])

   for n in range(1, limit):
      if isPrime(n):
        primes.append(n)

   sys.stdout.write(str(primes))
   sys.stdout.write('\n')

if __name__ == "__main__":
   main()
