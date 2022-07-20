import math                                 
#1)
print(math.ceil(20.5))                      #21
print(math.ceil(20.00))                     #20
print(math.ceil(20.01))                     #21
print(math.ceil(20.89))                     #21
#print(math.ceil(20.579,2))                 TypeError: ceil() takes exactly one argument (2 given)

#2)
print(math.floor(20.0))                     #20
print(math.floor(20.5))                     #20
print(math.floor(20.99))                    #20

#3)
print(math.pow(5,5))                        #3125.0
print(math.pow(50.0,2))                     #2500.0

#4)
print(math.sqrt(3125.0))                    #55.90169943749474

#5)
print(abs(-20))                             #20
print(abs(-20.50))                          #20.5
print(math.fabs(-20.50))                    #20.5
print(math.fabs(-20))                       #20.0

#6)
'''
math.copysign(x, y)
Return a float with the magnitude (absolute value) of x but the sign of y.
On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0.
'''
print(math.copysign(1,-1))                  #-1.0
print(math.copysign(1,0))                   #1.0
print(math.copysign(-1,1))                  #1.0
print(math.copysign(-1,-1))                 #-1.0
print(math.copysign(1.0, -0))               #1.0
print(math.copysign(1.0, -0.0))             #-1.0


#7)
print(math.factorial(5))                    #120
print(math.factorial(5.0))                  #120


#8)
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))            #0.9999999999999999
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))           #1.0


#9)
print(math.fmod(6,3))                       #0.0
print(math.fmod(6.5,3))                     #0.5


#10)math.frexp(x)
'''
math.frexp(x)
Return the mantissa and exponent of x as the pair (m, e).
m is a float and e is an integer such that x == m * 2**e exactly.
If x is zero, returns (0.0, 0), otherwise 0.5 <= abs(m) < 1.
This is used to “pick apart” the internal representation of a float in a portable way.
'''
print(math.frexp(2))                        #(0.5, 2)


#11)
print(math.gcd(3,6))                        #3
print(math.gcd(0,6))                        #6
print('lcm(3,6) : ',(3*6)/math.gcd(3,6))      #6.0


#12)math.isfinite(x)
'''
math.isfinite(x)
Return True if x is neither an infinity nor a NaN, and False otherwise. (Note that 0.0 is considered finite.)
'''
print(math.isfinite(0.0))                   #true
print(math.isfinite(1000))                  #true


#13)math.isinf(x)
'''
math.isinf(x)
Return True if x is a positive or negative infinity, and False otherwise.
'''
print(math.isinf(-1000000000000000000000000000000000))       #false
print(math.isinf(0))                                        #FALSE


#14)math.isnan(x)
'''
math.isnan(x)
Return True if x is a NaN (not a number), and False otherwise.
'''
print(math.isnan(1))                        #false
print(math.isnan(1.123456))                 #false


#15)math.isqrt(n)
'''
math.isqrt(n)
Return the integer square root of the nonnegative integer n.
This is the floor of the exact square root of n,or equivalently the greatest integer a such that a² ≤ n.

For some applications, it may be more convenient to have the least integer a such that n ≤ a²,
or in other words the ceiling of the exact square root of n.
For positive n, this can be computed using a = 1 + isqrt(n - 1).
'''
#print(math.isqrt(25))    present in python 3.8 version


#16)math.lcm(*integers)
'''
math.lcm(*integers)
Return the least common multiple of the specified integer arguments.
If all arguments are nonzero, then the returned value is the smallest positive integer that is a multiple of all arguments.
If any of the arguments is zero, then the returned value is 0. lcm() without arguments returns 1.

New in version 3.9.
'''

#17)math.nextafter(x, y)
'''
math.nextafter(x, y)
Return the next floating-point value after x towards y.

If x is equal to y, return y.

Examples:

math.nextafter(x, math.inf) goes up: towards positive infinity.
math.nextafter(x, -math.inf) goes down: towards minus infinity.
math.nextafter(x, 0.0) goes towards zero.
math.nextafter(x, math.copysign(math.inf, x)) goes away from zero.

See also math.ulp().

New in version 3.9.
'''

#18)math.comb(n, k)
'''
math.comb(n, k)
Return the number of ways to choose k items from n items without repetition and without order.
Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates to zero when k > n.
Also called the binomial coefficient because it is equivalent to the coefficient of k-th term
in polynomial expansionof the expression (1 + x) ** n.
Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

New in version 3.8.
'''

#19)math.perm(n, k=None)
'''
math.perm(n, k=None)
Return the number of ways to choose k items from n items without repetition and with order.

Evaluates to n! / (n - k)! when k <= n and evaluates to zero when k > n.

If k is not specified or is None, then k defaults to n and the function returns n!.

Raises TypeError if either of the arguments are not integers. Raises ValueError if either of the arguments are negative.

New in version 3.8.
'''

#20)math.log(x[, base])
'''
With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).
'''

#21)math.log2(x)
'''
Return the base-2 logarithm of x. This is usually more accurate than log(x, 2).

New in version 3.3.
'''

#22)math.log10(x)
'''
Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).
'''


#Trigonometric functions

#math.acos(x)
Return the arc cosine of x, in radians. The result is between 0 and pi.

#math.asin(x)
Return the arc sine of x, in radians. The result is between -pi/2 and pi/2.

#math.atan(x)
Return the arc tangent of x, in radians. The result is between -pi/2 and pi/2.

#math.atan2(y, x)
Return atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.

#math.cos(x)
Return the cosine of x radians.

#math.dist(p, q)
Return the Euclidean distance between two points p and q, each given as a sequence (or iterable) of coordinates. The two points must have the same dimension.

Roughly equivalent to:

sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
New in version 3.8.

#math.hypot(*coordinates)
Return the Euclidean norm, sqrt(sum(x**2 for x in coordinates)).
This is the length of the vector fromthe origin to the point given by the coordinates.

For a two dimensional point (x, y), this is equivalent to computing the hypotenuse of a right triangle using
the Pythagorean theorem, sqrt(x*x + y*y).

Changed in version 3.8: Added support for n-dimensional points. Formerly, only the two dimensional case was supported.

#math.sin(x)
Return the sine of x radians.

#math.tan(x)
Return the tangent of x radians.



#Angular conversion

#math.degrees(x)
Convert angle x from radians to degrees.

#math.radians(x)
Convert angle x from degrees to radians.

#Hyperbolic functions
Hyperbolic functions are analogs of trigonometric functions that are based on hyperbolas instead of circles.

#math.acosh(x)
Return the inverse hyperbolic cosine of x.

#math.asinh(x)
Return the inverse hyperbolic sine of x.

#math.atanh(x)
Return the inverse hyperbolic tangent of x.

#math.cosh(x)
Return the hyperbolic cosine of x.

#math.sinh(x)
Return the hyperbolic sine of x.

#math.tanh(x)
Return the hyperbolic tangent of x.



#Special functions

#math.erf(x)
Return the error function at x.

The erf() function can be used to compute traditional statistical functions such as the cumulative standard normal distribution:

def phi(x):
    'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0
New in version 3.2.

#math.erfc(x)
Return the complementary error function at x. The complementary error function is defined as 1.0 - erf(x). It is used for large values of x where a subtraction from one would cause a loss of significance.

New in version 3.2.

#math.gamma(x)
Return the Gamma function at x.

New in version 3.2.

#math.lgamma(x)
Return the natural logarithm of the absolute value of the Gamma function at x.

New in version 3.2.
