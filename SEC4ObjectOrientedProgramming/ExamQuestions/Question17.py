# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 17: Incorrect
What is the output of the following code?
"""

class Spam:
    def __init__(self, v):
        self.ham = v                #3
        self.__ham = self. ham + 1  #4

s = Spam(100)                       #5

print(s.ham, s.__ham)               #6

#i)Error in Line 6      #CORRECT!!!; *RE: variables prefixed with "__" are PRIVATE variables and CANNOT  be accessed
                        # outside the class!
#ii)Error in Line 4     #WRONG
#iii)Error in Line 5    #WRONG
#iv)100 101             #WRONG
#v)Error in Line 3      #WRONG

#*NOTE:
#   print(s.ham)    #100