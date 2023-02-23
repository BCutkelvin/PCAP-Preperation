# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 38: Incorrect
What is the output of the following code?

try:
    raise UndefinedException
except:
    pass
"""
try:
    raise UndefinedException            #1st - RE: UndefinedException is not part of the Exception Hiearchy! the try
                                        # will look for the exception "class" defined, moves to except clause
except:                                 #2nd - NOTE! LEGIT SYNTAX to not have except clause by ITSELF!; executes...
pass                                    #3rd - ...performs pass boolean, thus not output or details etc. 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#No output                                              #CORRECT!!
#Add () on Line 2(11) to fix the syntax error           #WRONG!
#SyntaxError:invalid syntax                             #WRONG!
#NameError: name 'UndefinedException' is not defined    #WRONG!