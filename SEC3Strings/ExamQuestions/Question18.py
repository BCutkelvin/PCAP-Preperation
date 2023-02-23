# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 18: Incorrect
What is the output of the following code?

print("C:\Program Files\Microsoft\Windows NT", end="")
print("\")
"""

print("C:\Program Files\Microsoft\Windows NT", end="")
print("\")     #OUTPUT: #SYNTAX ERROR: "\" is sued for escape characters ex "\n"; FIX: use "\\"
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#C:\Program Files\Microsoft\Windows NT\                                        #WRONG!
#Ignore escaped characters e.g. C: orgram Filesicorsoftindows NT               #WRONG!
#Syntax Error                                                                  #CORRECT!!
#Replace escaped characters with "?" e.g. C:?rogram Files?icrosoft?indows NT?  #WRONG!