# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 22: Incorrect
What is the output of the following code?

>>> spam, ham = 1, "ham"
>>> spam *= 3
>>> ham *= 3
>>> spam, ham
"""

spam, ham = 1, "ham"
spam *= 3
ham *= 3
print("spam, ham: ", spam, ham)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#(3, 0)                                                         #WRONG!
#TypeError: unsupported operand type(s) for *=: 'str' and 'int' #WRONG!
#SyntaxError: invalid syntax                                    #WRONG!
#3, hamhamham)                                                  #CORRECT!!