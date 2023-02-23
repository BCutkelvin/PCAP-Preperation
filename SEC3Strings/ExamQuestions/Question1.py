# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 1: Incorrect
What is the output of the following code?

spam.txt

spam ham eggs
spam.py

f = open('spam.txt', 'r')
if 'eggs' in f:
    print('Eggs found')
else:
    print('Eggs not found')
"""
#spam.txt
#   spam ham eggs

#spam.py
f = open('//Users/bryancutkelvin/PycharmProjects/PCAPprep/spam.txt', 'r') #open(...) returns file
if 'eggs' in f:                                                           #object NOT file content!
    print('Eggs found')
else:
    print('Eggs not found')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#SyntaxError: invalid syntax                            #WRONG!
#Eggs not found                                         #CORRECT!!
#Eggs found                                             #WRONG!
#TypeError: argument type TextOfWrapper not iterable    #WRONG!