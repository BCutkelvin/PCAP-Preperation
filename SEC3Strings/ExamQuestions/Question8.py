# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 8: Incorrect
What is the output of the following code?

>>> s = 'Hello World'
>>> for i in len(s):
...     s[i] = s[i].upper()
>>> s
"""

s = 'Hello World'
#print("len(s):", len(s))  #11; NOTE!! for in <value>, <value> cannot be a primitive (int0 value!!
for i in len(s):           #TypeError: 'int' object is not iterable;
    s[i] = s[i].upper()

s
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Hello World                                                #WRONG!
#Type Error: 'str' object does not support item assignment  #WRONG!
#HELLO WORLD                                                #WRONG!
#TypeError: 'int' object is not iterable                    #CORRECT!!



