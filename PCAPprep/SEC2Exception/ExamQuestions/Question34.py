# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 34: Incorrect
What is the output of the following code?

try:
    print("1", end='')
    raise Exception
    print("2", end='')
except BaseException:
    print("3", end='')
else:
    print("4", end='')
finally:
    print("5")
"""
try:
    print("1", end='')  #1st: prints ", "try" clause continues...
    raise Exception     #raise "Exception" object occurs...
    print("2", end='')
except BaseException:   #2nd: ..."closest hierarchy" Exception object occurs in except clause...
    print("3", end='')  #...thus except clause, performs print...
else:                   #...NOPE! (re: only if no exceptions, then run this code!)
    print("4", end='')
finally:                #3rd...RE!: if finally is presents, it specifies a "CLEANUP" Handler
    print("5")          #; thus if an exception occurs in any of the clauses and is not
                        # handled, the exception is temporarily saved and then the finally
                        #clase is executed!
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#1245                                           #WRONG!
#135                                            #CORRECT!!
#145                                            #WRONG!
#Namerror: name 'BaseException" is not defined  #WRONG!
#1235                                           #WRONG!