# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 11: Incorrect
What is the output of the following code?
"""
class Eggs:
    def __init__(self):
        print('Eggs', end=' ')
class Ham(Eggs):
    def __init__(self):
        print('Ham', end=' ')
class Spam(Ham):
    pass

s = Spam()


#i)Ham Eggs                                                             #WRONG!
#ii)Type Error: __init__() takes 1 positional argument but 0 were given #WRONG!
#iii)Eggs                                                               #WRONG!
#iv)No output                                                           #WRONG!
#v)Ham                                                                  #CORRECT!!

#RE:
#-Method Resolution Order: set of rule that construct linearization of classes
#   meaning: it will execute the first __init__() it finds in the class method resolution order.
#   ex. Spam.__mro__    #Ham (<class '__main__.Spam'>, <class '__main__.Ham'>, <class '__main__.Eggs'>, <class 'object'>)
