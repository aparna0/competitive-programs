#1)
'''
How many people must be there in a room to make the probability 100% that at-least two people in the room have same birthday?

Answer: 367 (since there are 366 possible birthdays, including February 29).
'''

#2)
'''
How many people must be there in a room to make the probability 50% that at-least two people in the room have same birthday?

Answer: 23
The number is surprisingly very low. In fact, we need only 70 people to make the probability 99.9 %.
'''

#write a prg to find how many number of peoples must be there can have same birthday for given probability
#formula : sqrt(2*365*log(1/(1-propability)))

import math
def findNoOfPersons(p):
    return math.ceil(math.sqrt(2*365*math.log(1/(1-p))))

p = float(input('Enter probability '))
print(findNoOfPersons(p))
