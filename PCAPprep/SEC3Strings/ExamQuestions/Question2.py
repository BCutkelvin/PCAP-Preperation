# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 2: Incorrect
What is the output of the following code?

"XYZ".join("123")
"""

print( "XYZ".join("123"))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#XYZ123                                 #WRONG!
#X123Y123Z                              #WRONG!
#1XYZ2XYZ3                              #CORRECT!!
#TypeError: can only join an iterable   #WRONG!
#123XYZ                                 #WRONG!