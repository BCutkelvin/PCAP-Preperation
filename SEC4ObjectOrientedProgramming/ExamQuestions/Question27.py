# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 27: Incorrect
Select the line number from the options(s) which will print Spam
"""
class Spam:
    def v0(self):
        print("Line 3:", __name__)

print("Line 4: ", __name__)

s = Spam()
s.v0()

print("Line 7: ", s.__class__.__name__)
print("Line 8: ", Spam.__name__)
#print("Line 9: ", s.__name__)   #ERROR! AttributeError: 'Spam' object has no attribute '__name__'

#1)Line 9   #WRONG!
#2)Line 4   #WRONG! "__main__"
#3)Line 7   #CORRECT! "Spam"
#4)Line 8   #CORRECT! "Spam"
#5)Line 3   #WRONG! "__main__"