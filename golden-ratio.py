#!/usr/bin/python

import sys

def main():
   if len(sys.argv) < 4:
      sys.stdout.writelines('Argument missing: command format should look like the following\n' +
          '  "python <program-name> limit[number] approxDecimal[number] step[number]"\n')
      return

   pairs = []

   limit = int(sys.argv[1])
   approxDecimal = int(sys.argv[2])
   step = float(sys.argv[3])

   b = 1
   while b < limit:
      b += step
      a = b + step
      while a < limit:         
         if round(a / b, approxDecimal) == round((a + b) / a, approxDecimal): # golden ratio conditions
            pairs.append({'a' : a , 'b' : b});
         a += step

   sys.stdout.write(str(pairs))
   sys.stdout.write('\n')

if __name__ == "__main__":
   main()
