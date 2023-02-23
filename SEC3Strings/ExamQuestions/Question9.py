# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 9: Incorrect
What is the output of the following code?

>>> sorted([5, "1", 100, "34"])
"""

print('sorted([5, "1", 100, "34"])', sorted([5, "1", 100, "34"])) #Error will occur if
                                                                  # attempting to compare
                                                                  # different data types
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#["1", "100", "34", "5"]                                            #WRONG!
#TypeError:'<' not supported between instances of 'str' and 'int'   #CORRECT!!
#[1, 5, 34, 100]                                                    #WRONG!
#[5, "1", "34", 100]                                                #WRONG!
#["1", 5, "34", 100]                                                #WRONG!



