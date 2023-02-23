# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 3 Strings - - - - - - -
"""
Question 25: Incorrect
What is the output of the following code?

"Spam Ham Eggs".index('Spam', 1)
"""
print("Spam Ham Eggs".index('Spam', 1))         #ERROR! ValueError: substring not found

#ValueError: substring not found                #CORRECT!!! RE: index('Spam', 1): starts SEARCH for "Spam" at index 1;
                                                #           observe "Spam" begins at index 0! so fail
#Spam                                           #WRONG!
#TypeError: index() takes 1 argument(2 given)   #WRONG!
#0                                              #WRONG!
#1                                              #WRONG!