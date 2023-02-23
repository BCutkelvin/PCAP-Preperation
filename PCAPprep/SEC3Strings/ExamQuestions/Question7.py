# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 7: Incorrect
What is the output of the following code?

spam = 'spam'
print(spam[0], end=' ')
spam[0]='x'
print(spam)
"""

spam = 'spam'
print(spam[0], end=' ')
spam[0]='x'     #BUG: You CANNOT assign a character to a String (index) object; RE: Strings are immutable!
print(spam)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#s.xpam                                                                 #WRONG!
#No output                                                              #WRONG!
#s followed by TypeError:'str' object does not support item assignment  #CORRECT!!
#s spam                                                                 #WRONG!


