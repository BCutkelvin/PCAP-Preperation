# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 24: Incorrect
What is the output of the following code?
"""
class Ham:
    def __init__(self):
        self.v1 = 1

class Spam(Ham):
    def __init__(self):
        self.v2 = 2

s = Spam()
print(s.v1, s.v2)

#i)0 2                                           #WRONG
#ii)Invalid syntax                               #WRONG
#iii)AttributeError:'Spam' has no attribute 'v1' #CORRECT!!
#iv)1 2                                          #WRONG
