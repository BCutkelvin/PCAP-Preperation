# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 43: Incorrect
What is the output of the following code?
"""
class Spam:
    def foo(self):
        print('Super Spam')

class Ham:
    def foo(self):
        print('Super Ham')

class Eggs(Spam, Ham):
    def foo(self):
        super().foo()

e = Eggs()
e.foo()



#i)Super Ham Super Spam     #WRONG
#ii)Super Spam              #CORRECT!!!
##iii)Super Ham             #WRONG
#iv)No output               #WRONG
#v)Super Spam Super Ham     #WRONG