# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
Which option will print (‘spam’, ‘eggs’) based on the following code?

try:
  raise Exception('spam', 'eggs')
except Exception as exception:
  << INSERT CODE HERE >>
"""
try:
    raise Exception('spam', 'eggs')
except Exception as exception:
    print(exception.args)              #CORRECT! - prints ('spam', 'eggs') using ___str__()
    print(exception)                   #CORRECT! - prints ('spam', 'eggs') using .args
    # print(exception.params)          #WRONG
    # print(exception.iterable[:])     #WRONG
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
