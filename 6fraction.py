'''
The fractions module provides support for rational number arithmetic.

A Fraction instance can be constructed from a pair of integers, from another rational number, or from a string.

class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(other_fraction)
class fractions.Fraction(float)
class fractions.Fraction(decimal)
class fractions.Fraction(string)
'''

from fractions import Fraction

print(Fraction(10,6))                       #5/3

print(Fraction(3.5))                        #7/2

print(Fraction(10/6))                       #7505999378950827/4503599627370496

print(Fraction(16, -10))                    #Fraction(-8, 5)

print(Fraction(123))                        #Fraction(123, 1)

print(Fraction())                           #Fraction(0, 1)

print(Fraction('3/7'))                      #Fraction(3, 7)

print(Fraction(' -3/7 '))                   #Fraction(-3, 7)
'''
>>> Fraction('1.414213 \t\n')
Fraction(1414213, 1000000)
>>> Fraction('-.125')
Fraction(-1, 8)
>>> Fraction('7e-6')
Fraction(7, 1000000)
>>> Fraction(2.25)
Fraction(9, 4)
>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)
>>> from decimal import Decimal
>>> Fraction(Decimal('1.1'))
Fraction(11, 10)
'''
