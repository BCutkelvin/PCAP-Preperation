# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 24: Incorrect
What is the output of the following code?

def f():
    try:
        print('try ', end='')
        raise ArithmeticError
    except:
        print('except ', end='')
        raise AssertionError
    finally:
        print('finally')
        return
f()
"""
def f():
    try:
        print('try ', end='')
raise ArithmeticError                        #NOTE: although raise "assertion" is called it continues the try clause
    except:
        print('except ', end='')
        raise AssertionError                 #NOTE: although raise "assertion" is called it continues the except clause
    finally:
        print('finally')
        return

f()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#try except <AssertionError logs> finally                           #WRONG!
#try <ArithmeticError logs> except <AssertionError logs> finally    #WRONG!
#try except finally                                                 #CORRECT!! RE!: if finally is presented, it
                                                                    # specifies a "CLEANUP" Handler; thus if an
                                                                    # exception occurs in any of the clauses and is not
                                                                    # handled, the exception is temporarily saved and
                                                                    #then the finally clause is executed!
#try except <AssertionError logs>                                   #WRONG!
#try except finally <AssertionError logs>                           #WRONG!
#try except finally <ArithmeticError logs> <AssertionError logs>    #WRONG!

