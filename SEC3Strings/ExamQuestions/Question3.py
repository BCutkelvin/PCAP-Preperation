# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 3: Incorrect
What is the output of the following code?

t = "Spam Ham"
print(t.find("Ham", 0) == t.index("Ham", 0))
print(t.find("Eggs", 0) == t.index("Eggs", 0))
"""
t = "Spam Ham"
print(t.find("Ham", 0) == t.index("Ham", 0))
print(t.find("Eggs", 0) == t.index("Eggs", 0))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#True False                                                                     #WRONG!
#True will be printed followed by TypeError: find() takes 1 argument( 2 given)  #WRONG!
#True True                                                                      #WRONG!
#True will be printed followed by ValueError: substring not found               #CORRECT!!