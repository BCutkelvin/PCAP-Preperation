# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 18: Incorrect
What is the output of the following code?
"""
class MyClass:
    FOO = 100

    def __init__(self):
        self.bar = []

    def add(self, p):
        self.bar.append(p)

d, e = MyClass(), MyClass()
d.add('spam')
e.add('ham')
e.FOO = 200
MyClass.FOO = 300

print(d.bar, d.FOO, e.bar, e.FOO)


#i)['spam']100['ham']300
#ii)['spam']300['ham']300
#iii)['spam']100['ham']200
#iv)['spam']300['ham']200