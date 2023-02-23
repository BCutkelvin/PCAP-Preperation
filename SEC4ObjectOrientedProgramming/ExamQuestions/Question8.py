# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 8: Incorrect
What is the output of the following code?
"""

def spam():
    h = Ham()       #compile time error: Unresolved reference 'Ham'
    h.eggs()

    class Ham:      #*RE: A class CAN be declared inside function definitions!!
        def eggs(self):
            print('Hello World')
    return

spam()

#i)SyntaxError: invalid syntax                                             #WRONG!
#ii)Hello World                                                            #WRONG!
#iii)UnboundLocalError: local variable 'Ham' referenced before assignment  #CORRECT!!!
#iv)No Output                                                              #WRONG!

"""
#*RE: this is legit!
def spam():
    class Ham:
        def eggs(self):
            print("Hello World")
    return Ham()
"""