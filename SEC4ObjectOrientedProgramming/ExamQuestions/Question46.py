# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 46: Incorrect
What is the output of the following code?
"""
class Spam:
  HAM = 1

  def __init__(self, v=2):
    self.v = v + Spam.HAM
    Spam.HAM += 1

a = Spam()
b = Spam(3)

print(a.v, b.v)

#i)TypeError:__init__() missing 1 required positional argument: 'v' #WRONG
#ii)3 4                                                             #WRONG
#iii)3 5                                                            #CORRECT!!
#iv)3 3                                                             #WRONG
