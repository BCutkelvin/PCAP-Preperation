# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 22: Incorrect
What will happen if spam.py is run?

# spam.py

try:
  print(x)
except:
  print("An exception occurred")
    pass
"""
# spam.py

try:
    print(x)    #NOTE: IDE (precompile) gives error "Unresolved reference 'x'"
                                    #1st raises NameError: name 'x; is not defined; goes to except...
except:                             #2nd executes logic in except cluse...
    print("An exception occurred")  #3rd prints info

#None will be printed                               #WRONG!;
#The script will run but will not print anything    #WRONG!
#compile time error                                 #WRONG!
#an exception occurred will be printed              #CORRECT!!
