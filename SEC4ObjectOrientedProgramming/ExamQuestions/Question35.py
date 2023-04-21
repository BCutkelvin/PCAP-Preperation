# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 35: Incorrect
What is the output of the following code?
"""
def foo(self, p):
    print('Hello', p)

class Spam:     #observe class definition CAN occur below definition of a method, even one it will use!
    bar = foo   #*NOTE! "INSTANCE "VARIABLE NAME" ASSIGNMENT"!

s = Spam()
s.bar('World')  #which is really s.foo(...) ...

#i)SyntaxError: invalid syntax              #WRONG
#ii)NameError: name 'foo' is not defined    #WRONG
#iii)No output                              #WRONG
#iv)Hello World                             #CORRECT!!
