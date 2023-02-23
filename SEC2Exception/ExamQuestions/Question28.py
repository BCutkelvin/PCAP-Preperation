        # - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 28: Incorrect
What is the output of the following code?

try:
    raise IOError
except IOError as e:
    raise RuntimeError from e
"""
try:
    raise IOError                   #1st - raises "IOError" exception, now see if there is a matching except clause...
except IOError as e:                #2nd - ...from raised IOError exception; matched! this except clause performs...
    raise RuntimeError from e       #OUTPUT! "RuntimeError"; 3rd... raises RuntimeError exception
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#SyntaxError: Invalid Syntax        #WRONG!
#No output                          #WRONG!
#RuntimeError                       #CORRECT!!
#IOError                            #WRONG!
