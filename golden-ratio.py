#!/usr/bin/python

import sys


FI = 1.61803398874989

def get_function_name(arguments):
   return '' if len(arguments) < 2 else arguments[1]

def check_parameters(arguments):
   f_name = get_function_name(arguments)
   if f_name == 'pairs':
      if len(arguments) == 5:
         return True
      else:
         sys.stdout.write('Argument missing: command format should look like the following\n' +
         '  "python golden-ratio.py pair limit<number> approxDecimal<number> step<number>"\n')
         return False
   elif f_name == 'split':
      if len(arguments) == 4:
         return True
      else:
         sys.stdout.write('Argument missing: command format should look like the following\n' +
         '  "python golden-ratio.py sum<number> approxDecimal<number>"\n')
         return False
   else:
      sys.stdout.write('Unknown function "' + f_name + '"\n')
      return False

def split(arguments):
   sum = int(arguments[2])
   approxDecimal = int(arguments[3])
   a = round(sum / FI, approxDecimal)
   b = sum - a
   sys.stdout.write('a: ' + str(a) + ' , b: ' + str(b) + '\n')

def pairs(arguments):
   pairs = []

   limit = int(arguments[2])
   approxDecimal = int(arguments[3])
   step = float(arguments[4])

   b = 1
   while b < limit:
      b += step
      a = b + step
      while a < limit:         
         if round(a / b, approxDecimal) == round((a + b) / a, approxDecimal): # golden ratio conditions
            pairs.append({'a' : a , 'b' : b});
         a += step

   if len(pairs) == 0:
      sys.stdout.write('No pair found\n')
   else:
      for pair in pairs:
         sys.stdout.write('a: ' + str(pair.get('a')) + ' , b: ' + str(pair.get('b')))
         sys .stdout.write('\n')

def main():
   sys.stdout.write('[Golden-ratio irrational proportion value is ' + str(FI) + '..]\n')

   if not check_parameters(sys.argv):
      return

   f_name = get_function_name(sys.argv)
   if f_name == 'pairs':
      pairs(sys.argv)
   elif f_name == 'split':
      split(sys.argv)

if __name__ == "__main__":
   main()
