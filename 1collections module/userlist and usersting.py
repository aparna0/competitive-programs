'''
UserList objects¶

This class acts as a wrapper around list objects. It is a useful base class for your own list-like classes which can inherit
from them and override existing methods or add new ones. In this way, one can add new behaviors to lists.

The need for this class has been partially supplanted by the ability to subclass directly from list; however,
this class can be easier to work with because the underlying list is accessible as an attribute.

class collections.UserList([list])
Class that simulates a list. The instance’s contents are kept in a regular list, which is accessible via the
dataattribute of UserList instances. The instance’s contents are initially set to a copy of list, defaulting to the empty list [].
list can be any iterable, for example a real Python list or a UserList object.

In addition to supporting the methods and operations of mutable sequences, UserList instances provide the following attribute:

data
A real list object used to store the contents of the UserList class
'''

'''
# Python program to demonstrate
# userstring
  
  
from collections import UserString
  
  
d = 12344
  
# Creating an UserDict
userS = UserString(d)
print(userS.data)
  
  
# Creating an empty UserDict
userS = UserString("")
print(userS.data)
'''

# Python program to demonstrate
# userstring
  
  
from collections import UserString
  
  
d = 12344
  
# Creating an UserDict
userS = UserString(d)
print(userS.data)
  
  
# Creating an empty UserDict
userS = UserString("")
print(userS.data)
'''
= RESTART: F:/python/python_programs/5competetive programming/collections module demo/userlist and usersting.py
12344

'''



# Python program to demonstrate
# userstring
   
  
from collections import UserString
   
  
# Creating a Mutable String
class Mystring(UserString):
      
    # Function to append to
    # string
    def append(self, s):
        self.data += s
          
    # Function to rmeove from 
    # string
    def remove(self, s):
        self.data = self.data.replace(s, "")
      
# Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)
  
# Appending to string
s1.append("s")
print("String After Appending:", s1.data)
  
# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)

'''
Original String: Geeks
String After Appending: Geekss
String after Removing: Gkss
>>> 
'''
