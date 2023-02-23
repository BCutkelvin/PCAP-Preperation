# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 37: Incorrect
What is the output of the following code?

try:
    raise UndefinedException
except NameError:
    print('NameError')
except UndefinedException:
    print('UndefinedException')
except:
    pass
"""
try:
    raise UndefinedException        #1st - try clause raises "UndefinedException"...
except NameError:                   #2nd - ...except clause occurs because of raise in "try" clause
    print('NameError')              #3rd - ...thus, print "NameError" occurs
except UndefinedException:          #NOTE: this except clause does not occur; the raise will look for the class it is
print('UndefinedException')         # calling; UndefinedException is not part of the Exception Hiearchy!
except:
    pass
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#NameError                      #CORRECT!!
#UndefineException              #WRONG!
#SyntaxError: invalid syntax    #WRONG!
#No output                      #WRONG!