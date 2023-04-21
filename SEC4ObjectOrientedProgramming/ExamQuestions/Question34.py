# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 34: Incorrect
What is the output of the following code?
"""
class A(object):
    pass

class C(A, A):  #NOTE: duplicate base class A; Duplicate bases class are NOT allowed!
    pass

#i)NameError:name 'object' is not defined   #WRONG
#ii)No output                               #WRONG
#iii)SyntaxError: invalid syntax            #WRONG
#iv)TypeError: duplicate base class A       #CORRECT!!