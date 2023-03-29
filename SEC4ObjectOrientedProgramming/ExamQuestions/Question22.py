# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 22: Incorrect
What is the output of the following code?
"""
class X:
    def spam(self): pass

ham = X.spam

print(ham.__name__) #NOTE: __name__ refers to the nme of the class, function, method, description or generator instance;
                    # thus the name = X.spam, where "spam" is the instance
#i)X.spam           #WRONG
#ii)ham             #WRONG
#iii)SyntaxError    #WRONG
#iv)Spam            #CORRECT!!
