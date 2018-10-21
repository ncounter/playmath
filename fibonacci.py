#!/usr/bin/python

import sys

def main():
   if len(sys.argv) < 2:
      sys.stdout.writelines('Argument missing: command format should look like the following\n' +
          '  "python <program-name> limit[number]"\n')
      return

   fibonacci = [1, 1]

   limit = int(sys.argv[1])

   n = 0
   while n < limit:
      n = fibonacci[len(fibonacci)-2] + fibonacci[len(fibonacci)-1]
      if n < limit:
        fibonacci.append(n)

   sys.stdout.write(str(fibonacci))
   sys.stdout.write('\n')

if __name__ == "__main__":
   main()
