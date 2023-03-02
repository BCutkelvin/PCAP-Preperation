# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 16: Incorrect
What is the output of the following code?
"""

class Ham:
    def __init__(self):
        print('Ham', end=' ')
class Eggs:
    def __init__(self, end=' '):
        print('Eggs')
class Spam(Ham, Eggs):
    pass

s = Spam()

#i)Eggs         #WRONG!
#ii)Ham         #CORRECT!!
#iii)No output  #WRONG!
#iv)Ham Eggs    #WRONG!

#*RE: MRO (Method Resolution Order) -
#   -Class weill execute the first __init__() it finds in the class
#ex
print("Spam.__mro__: ", Spam.__mro__)   #(<class '__main__.Spam'>, <class '__main__.Ham'>, <class '__main__.Eggs'>, <class 'object'>)
