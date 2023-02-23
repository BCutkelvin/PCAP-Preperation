# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 5: Incorrect
What is the output of the following code?

t = "Spam Ham"
print(t.rfind("am") == t.find("am"))
print(t.rfind("am", 3) == t.find("am", 3))
print(t.rfind("am", -3) == t.find("am", -3))
"""

t = "Spam Ham"                                 #RE!: .find() = lowest index; .rfind() = highest index; these only take 1 argument
print(t.rfind("am") == t.find("am"))           #(6, 2)
print(t.rfind("am", 3) == t.find("am", 3))     #(6, 6)
print(t.rfind("am", -3) == t.find("am", -3))   #(6, 6)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#True True True                                                                 #WRONG!
#False False False                                                              #WRONG!
#False True True                                                                #CORRECT!!
#True will be printed followed by TypeError: rfind takes 1 argument (2 given)   #WRONG!



