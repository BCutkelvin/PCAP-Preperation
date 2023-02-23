# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 6: Incorrect
What is the output of the following code?

sorted(['banana', 'pear', 'grapes', 'apple'], key=lambda x: x[::-1])
"""

print( sorted(['banana', 'pear', 'grapes', 'apple'], key=lambda x: x[::-1]) ) #RE! [::-1] 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#['apple', 'banana', 'grapes', 'pear']                          #WRONG!
#Type Error: 'key' is an invalid keyword argument for sorted()  #WRONG!
#SyntxError: invalid syntax                                     #WRONG!
#['banana', 'apple', 'pear', 'grapes']                          #CORRECT!!


