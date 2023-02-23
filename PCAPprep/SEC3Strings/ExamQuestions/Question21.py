# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 21: Incorrect
What is the output of the following code?

spam = [4*(3+5), 4*3+5, 4+3*5, (4+3)*5]
spam.sort(reverse=True)
spam
"""

spam = [4*(3+5), 4*3+5, 4+3*5, (4+3)*5]
spam.sort(reverse=True)
print("spam: ", spam)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#TypeError: 'reverse' is an invalid keyword argument for sort() #WRONG!
#[35, 19, 17, 32]       #WRONG!
#[35, 32, 19, 17]       #CORRECT!! #RE: reverse() reverses the List elements in place; but it DOES NOT return a new List
#[17, 19, 32, 35]       #WRONG!
#[32, 17, 19, 35]       #WRONG!