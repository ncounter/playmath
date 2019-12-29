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
         '  "python golden-ratio.py pairs limit<number> approxDecimal<number> step<number>"\n')
         return False
   elif f_name == 'split':
      if len(arguments) == 4:
         return True
      else:
         sys.stdout.write('Argument missing: command format should look like the following\n' +
         '  "python golden-ratio.py split sum<number> approxDecimal<number>"\n')
         return False
   else:
      sys.stdout.write('Unknown function "' + f_name + '"\n')
      sys.stdout.write('Available functions are\n'+
                        '- pairs: find pairs of number below the given limit<number>, the approxDecimal<number> approximation '+
                          'and the step<number> pace to move during the research\n' +
                        '- split: bisect the given sum<number> into two numbers where the results are in a "golden ratio" ' +
                          'relationship, respecting the given approxDecimal<number> approximation\n')
      return False

def split(arguments):
   sum = float(arguments[2])
   approxDecimal = int(arguments[3])
   a = round(sum / FI, approxDecimal)
   b = sum - a

   sys.stdout.write('a = ' + str(a) + ' , b = ' + str(b) +
           ' , a/b = ' + str(a / b) +
           ' ==> round(a/b, ' + str(approxDecimal) + ') = ' + str(round(a / b, approxDecimal)))
   sys.stdout.write('\n')

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
         sys.stdout.write('a = ' + str(pair.get('a')) + ' , b = ' + str(pair.get('b')) +
           ' , a/b = ' + str(pair.get('a') / pair.get('b')) +
           ' ==> round(a/b, ' + str(approxDecimal) + ') = ' + str(round(pair.get('a') / pair.get('b'), approxDecimal)))
         sys.stdout.write('\n')

def main():
   sys.stdout.write('*************************************************************\n')
   sys.stdout.write('[Golden-ratio irrational proportion value is ' + str(FI) + '..]\n')
   sys.stdout.write('*************************************************************\n')

   if not check_parameters(sys.argv):
      return

   f_name = get_function_name(sys.argv)
   if f_name == 'pairs':
      pairs(sys.argv)
   elif f_name == 'split':
      split(sys.argv)

if __name__ == "__main__":
   main()
