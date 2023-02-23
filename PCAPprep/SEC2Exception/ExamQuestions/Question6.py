# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
Which option(s) will print ELSE given the following code?

try:
    <<< INSERT CODE HERE >>>
except ZeroDivisionError:
  print('ZeroDivisionError')
except TypeError:
    print('TypeError')
else:
    print('ELSE')
"""
try:
    pass                      #CORRECT ANSWER!
    # insert "blank"          #WRONG! BUG: IndentationError: expected an indented blockchoice 2
    # raise TypeError         #WRONG! Output: "TypeError"
    # raise ZeroDivisionError #WRONG! Output: "Zero Division Error"
    # raise                   #WRONG! BUG: No exception to reraise
    # raise Exception         #WRONG! Raises "Exception"
except ZeroDivisionError:
    print('ZeroDivisionError')
except TypeError:
    print('TypeError')
else:
    print('ELSE')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
