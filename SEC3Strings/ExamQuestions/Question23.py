# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 23: Incorrect
What is the output of the following code?

d = { 'zero':0, 'one':1, 'three':3, 'two':2 }
for k in sorted(d.keys()):
    print(d[k], end=' ')
"""

d = {'zero': 0, 'one': 1, 'three': 3, 'two': 2}
for k in sorted(d.keys()):  # RE: sorted() SORT KEYS ALPHABETICALLY (LEXICOGRAPHICAL)
    print(d[k], end=' ')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# zero one two three                             #WRONG!
# TypeError: sorted expected 2 arguments, got 1  #WRONG!
# 0 1 2 3                                        #WRONG!
# 1 3 2 0                                        #CORRECT!!
# one three two zero                             #WRONG!
