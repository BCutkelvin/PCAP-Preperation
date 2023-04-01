# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 25: Incorrect
Select the option(s) which will return the dictionary or other mapping object used to store an object’s (writable)
attributes of the following code
"""
class Person:
    name = "John"
    age = 36
    country = "USA"

p = Person()

#i)print("p.__dict__: ", p.__dict__)        #WRONG; returns and empty dictionary {}
#ii)(print("vars(p): ", vars(p))            #WRONG; returns and empty dictionary {}
#iii)print("vars(Person): ", vars(Person) ) #CORRECT!!; returns the dictionary as:
#    {'__module__': '__main__', 'name': 'John', 'age': 36, 'country': 'USA', '__dict__': <attribute '__dict__' of
#    'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
#print("Person.__dict__:", Person.__dict__)  #CORRECT; returns the dictionary as:
#   {'__module__': '__main__', 'name': 'John', 'age': 36, 'country': 'USA', '__dict__': <attribute '__dict__' of
#   'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}