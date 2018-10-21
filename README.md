# playmath
An archive of maths problems, famous topics, or just some function to compute well known type of numbers.

# How to use

## Prime numbers
It returns the list of `prime numbers` below the number passed as an argument.
```
cd playmath
python prime-numbers.py 30
```
#### Expected output
```[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]```


## Fibonacci

**Fibonacci sequence**

`1 1 x1 x2 x3 x4 x5 .. xi .. xn` with *xi = x(i-2) + x(i-1)*

It returns the `Fibonacci sequence` cut below the number passed as an argument.
```
cd playmath
python fibonacci.py 30
```
#### Expected output
```[1, 1, 2, 3, 5, 8, 13, 21]```


## Golden-ratio

**Golden ratio** condition

**`a / b = (a + b) / a`**  = ~*1.61803398874989*

### Pairs
It returns all `pairs of numbers` those with the `golden ratio` proportion below the number passed as the first numeric argument, according to the `deciman approximation` passed as the second numeric argument and the pace given by the third numeric argument to move among all the numbers in the set (from 1 to the given limit one - the first numeric argument).

```
cd playmath
python golden-ratio.py pairs 30 2 0.5
```
#### Expected output
```
a: 10.5 , b: 6.5
a: 17.0 , b: 10.5
a: 21.0 , b: 13.0
a: 23.5 , b: 14.5
a: 27.5 , b: 17.0
```

### Split
It returns the `pair of numbers` those with the `golder ratio` proportion for the given number passed as the first numeric argument, according to the `decimal approximation` passed as the second numeric argument.
```
cd playmath
python golden-ratio.py split 9 4
```
#### Expected output
```a: 5.5623 , b: 3.4377```
