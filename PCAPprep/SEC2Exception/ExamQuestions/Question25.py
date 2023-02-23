# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 25: Incorrect
What is the output of the following code?

def f():
    try:
        raise ArithmeticError
    except:
        raise AssertionError
    finally:
        raise AttributeError
    return
f()
"""
def f():
    try:
        raise ArithmeticError   #NOTE: although raise "assertion" is called it continues the try clause; thus during
    except:                     # ArithmeticError handling, another exception "AssertionError" occurred, so...
        raise AssertionError    #NOTE: although raise "assertion" is called it continues the except clause;
    finally:                    # then RE! if finally is presented, it specifies a "CLEANUP" Handler; thus
        raise AttributeError    # finally clause is executed!
    return

f()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#SyntaxError: invalid syntax    #WRONG!
#ArithmeticError                #CORRECT!!
#No Output                      #WRONG!
#AssertionError                 #CORRECT!!
#Attribute Error                #CORRECT!!