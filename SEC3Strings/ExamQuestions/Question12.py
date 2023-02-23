# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 12: Incorrect
What is the output of the following code?

def reverse(word):
    return word[::-1]
print(sorted(['banana', 'pear', 'grapes', 'apple'], key=reverse))
"""

def reverse(word):
    return word[::-1]   #RE: [::-1] reverses a list

print("\n1st, sorted(['banana', 'pear', 'grapes', 'apple']): ", sorted(['banana', 'pear', 'grapes', 'apple'] ) )

print("\n2nd, let argument, key = reverse()...")
print("reverse(['banana', 'pear', 'grapes', 'apple']):\t", reverse(['banana', 'pear', 'grapes', 'apple']))

print("\n3rd, finally using 'key=':\t\t\t\t\t\t", sorted(['banana', 'pear', 'grapes', 'apple'], key=reverse))
#['banana', 'apple', 'pear', 'grapes']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#['pear', 'grapes', 'banana', 'apple']                      #WRONG!
#['grapes', 'pear', 'apple', 'banana']                      #WRONG!
#['banana', 'apple', 'pear', 'grapes']                      #CORRECT!!
#TypeError: 'key' is an invalid keyword argument for sortd()#WRONG!