# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 21: Incorrect
What is the output of the following code?

try:
    abcd
    efgh
except:
    pass
"""
try:
    abcd    #NOTE: IDE says (precompile error) "unresolved reference 'abcd'...1st raises exception "NameError"...
    efgh    #NOTE: IDE says (precompile error) "unresolved reference 'efgh'
except:     #2nd...proceeds with exception...
    pass    #3rd...null operation, just means "pass" (we've seen this before ;) )
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Add () on Line 2 and 3 to fix the syntax error     #WRONG
#NameError:name 'UndefinedException' is not defined #WRONG
#SyntaxError: invalid syntax                        #WRONG
#No output                                          #CORRECT!!