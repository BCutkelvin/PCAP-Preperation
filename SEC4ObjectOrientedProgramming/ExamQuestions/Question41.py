# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 41: Incorrect
Select the choices which will return TRUE?
"""
class X:
    pass


class Y:
    pass


class Z(X, Y):
    pass


x, y, z = X(), Y(), Z()

# i)isinstance( (list, X, Y), z )           #WRONG; isinstance() arg 2 must be a type or tuple of types
# ii)isinstance(z, X) and isinstance(z, Y)  #CORRECT!!
# iii)isinstance(z, X, Y)                   #WRONG; isinstance expected 2 arguments, got 3
# iv)isinstance(z, (list, X, Y) )           #CORRECT!!
# v)isinstance( X, z) and isinstance(Y, z)  #WRONG; TypeError: isinstance() arg 2 must be a type or tuple of types

#*RE: isinstance(object, classinfo) is object  an instance of classinfo
#ex. isinstance(z, X) and isinstance(z, Y) #True; since Z has argument of X, where x is instance of X(); same for Y
#ex. isinstance(X, z) and isinstance(Y, z) #WRONG! incorrect order

#*RE: isinstance is a tuple, ie. isinstance(object, classinfo, classinfo), return True if object is an instance of
# any of the types.

