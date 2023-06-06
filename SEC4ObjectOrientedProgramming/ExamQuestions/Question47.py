# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 47: Incorrect
What is the output of the following code?
"""
class Ham:
    v = 1
    def v0(self):
        return self.v

class Spam(Ham):
    v = 2

s = Spam()
h = Ham()

print(s.v0(), h.v0())


#i)2 2                                                  #WRONG
#ii)AttributeError: 'Spam' object hs no attribute 'v0'  #WRONG
#iii)1 1                                                #WRONG
#iv)2 1                                                 #CORRECT!!

