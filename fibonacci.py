#!/usr/bin/python

import sys

def main():
   fibonacci = [1, 1]

   n = 0
   while n < int(sys.argv[1]):
      n = fibonacci[len(fibonacci)-2] + fibonacci[len(fibonacci)-1]
      if n < int(sys.argv[1]):
        fibonacci.append(n)

   sys.stdout.write(str(fibonacci))
   sys.stdout.write('\n')

if __name__ == "__main__":
   main()
