# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 6: Incorrect
Select the choices which will return TRUE?
"""
class X:  # *NOTE: issubclas(class, classinfo) - a class is a subclass of classinfo or of itself
    pass

class Y:
    pass

class Z(X, Y):
    pass

# i)print("issubclass(Z, (list, X, Y))", issubclass(Z, (list, X, Y)))                        #CORRECT!!
# ii)print("issubclass(X, Z) and issubclass(Y, Z): ", issubclass(X, Z) and issubclass(Y, Z)) #WRONG!
# iii)print("issubclass(Z, X, Y: ", issubclass(Z, X, Y))                                     #WRONG!; TypeError: issubclass expected 2 arguments, got 3
# iv)print("issubclass(Z, X) and issubclass(Z, Y): ", issubclass(Z, X) and issubclass(Z, Y)) # CORRECT!!
