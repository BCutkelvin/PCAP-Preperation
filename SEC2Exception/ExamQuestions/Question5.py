# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
What is the output of the following code?

try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))
"""
try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))      #0  - WRONG!
                            #3  - WRONG!
                            #2  - WRONG!
                            #1  - WRONG!
                            #CORRECT! AttributeError: 'Exception' object hasno attribute 'args'
    #here is how to veryify and fix:
    someVarToGetExceptionArgs = e.args
    print(f'someVarToGetExceptionArgs: {someVarToGetExceptionArgs}')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
