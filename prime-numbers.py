#!/usr/bin/python

import sys

def isDivisorOf(d, n):
   return n%d == 0

def sumSingleDigits(n):
   sum = 0
   for i in range(0, len(str(n))):
      sum += int(str(n)[i])
   return sum

def minimizeBySum(n):
   while len(str(n)) > 1:
      n = sumSingleDigits(n)
   return n

# isPrime receives only odd numbers, there is no need to check for even numbers or for (n%2==0)
def isPrime(n):
   if n == 1:
      return True

   # let's just do the skipping only after the first ten numbers
   if n > 10:
      # skip all numbers divisible by 3 because the sum of single digits is a multiple of 3
      if minimizeBySum(n) % 3 == 0:
         return False
      # skip all odd numbers divisible by 5
      if str(n).endswith('5') and n > 5:
         return False

   # divisor range from 3 with a step of 2 so we skip all even divisors: if divisor was even,
   # we would have an even number, and even means it can be divided always also by the number 2,
   # so it couldn't be a prime number, definitely.
   # highest divisor 'i' cannot be no greater than the half of the number 'n',
   # as 'n' would then be a multiple by 2 of 'i': setting the max range value up to '(n/2)-1' then
   for i in range(3, (n/2)+1, 2) :
      if isDivisorOf(i, n):
         return False

   return True

def main():
   if len(sys.argv) < 2:
      sys.stdout.writelines('Argument missing: command format should look like the following\n' +
          '  "python prime-numbers.py limit<number>"\n')
      return

   primes = []

   # by default 1 argument as a minimal value and it is the upper limit
   limit = int(sys.argv[1])
   min_limit = 3

   # if there are more arguments, the order matters: min_limit first, then upper limit
   if len(sys.argv) == 3:
       min_limit = int(sys.argv[1])
       limit = int(sys.argv[2])

   # start from the first odd value
   if min_limit % 2 == 0:
       min_limit = min_limit + 1

   # start from 3 as a minimum if set differently
   if min_limit < 3:
       min_limit = 3

   primes.append(2) # because we know the first prime number (and the only even one) is number 2

   # move ahead of a "step of 2 numbers", starting from the first odd value, to skip all even values
   for n in range(min_limit, limit+1, 2):
      if isPrime(n):
        primes.append(n)

   sys.stdout.write('## ' + str(len(primes)) + ' prime numbers found ##')
   sys.stdout.write('\n')
   sys.stdout.write(str(primes))
   sys.stdout.write('\n')

if __name__ == "__main__":
   main()
