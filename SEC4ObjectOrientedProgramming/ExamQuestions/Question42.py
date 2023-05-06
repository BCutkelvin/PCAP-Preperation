# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 42: Incorrect
Which of the option(s) below are valid given the following code?
"""
class Spam:
    #__ham, ham = '__ham', 'ham'  #move to bottom for readability...

    def __eggs(self):
        pass

    eggs = __eggs

    __ham, ham = '__ham', 'ham'


s = Spam()
#INSERT CODE HERE

#i)print(s.__module__)                #CORRECT!!; => s.__module__ __main__
#ii)print(__module__)                 #WRONG; Unresolved reference '__module__'
#iii)print(Spam.__module__)           #CORRECT!!; => s.__module__ __main__
#iv)print("s.__Spam_eggs.__module__") #CORRECT!!; => Spam.__module__ __main__
#v)print(s.ham.__module__: )          #WRONG; AttributeError: 'str' object has no attribute '__module__'
#vi)print("s.eggs.__module__")        #CORRECT!!; => s.eggs.__module__