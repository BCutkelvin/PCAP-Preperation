# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - PCEP-31-03 4.2 - Employ class and class and object properties - - - - - - -
""" - - - - - - - properties: __module__- - - - - - - """
import sys as sys


# __module__ is where every Python class has a built-in class attribute which is the name of the module in which the
# class is defined
# -each class and function has a __module__attribute that returns the name of the module in which the cass is defined

# ex how to return the list of modules that have been imported in your session
print("sys.modules: \t", sys.modules)

#ex Given a class, return the name of the module class was defined:
class SomeClass:
    print("\nGiven a class SomeClass, then SomeClass.__module__:")
    pass

print(SomeClass.__module__)
print(SomeClass.__class__.__module__)
