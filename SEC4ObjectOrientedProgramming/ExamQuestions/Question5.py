# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 5: Incorrect
What is the output of the following code?
"""
def spam():
    class Ham:                  #***NOTE! class can be declared inside function definitions ***
        def eggs(self):
            print('Hello World')
    return Ham()

spam().eggs()

#i)AttributeError: spam() has no attribute 'eggs'   #WRONG!
#ii)No output                                       #WRONG!
#iii)Hello World                                    #CORRECT!!
#iv)SyntaxError: invalid syntax                     #WRONG!
