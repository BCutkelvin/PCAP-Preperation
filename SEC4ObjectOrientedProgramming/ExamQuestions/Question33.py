# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 33: Incorrect
What is the output of the following code?
"""
class Foo:
    bar = 'spam'

f1 = Foo()
f2 = Foo()
f2.bar = 'ham'
Foo.bar = 'eggs'

print(f1.bar, f2.bar, Foo.bar)

# i)eggs eggs eggs
# ii)spam ham eggs
# iii)eggs ham eggs
# iv)AttributeError: type object 'Foo' has no attribute 'bar'