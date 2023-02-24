# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 9: Incorrect
Which of the option(s) below are valid calls given the code below?
"""


class Spam:
    __ham = 0

    def __eggs(self):
        __ham = 100
        return __ham

    eggs = __eggs


s = Spam()

#---INSERT CODE HERE---

#i)print("s.__ham: ", s.__ham )                    #WRONG! AttributeError: 'Spam' object has no attribute '__ham'
#ii)print("s.eggs(): ", s.eggs() )                 #CORRECT!! s.eggs():  100
#iii)print("s.__eggs(): ", s.__eggs() )            #WRONG! AttributeError: 'Spam' object has no attribute '__eggs'
#iv)print("s._Spam__ham: ", s._Spam__ham )         #CORRECT!! s._Spam__ham:  0
#V)print("s._Spam_eggs(): ", s._Spam_eggs() )      #WRONG! AttributeError: 'Spam' object has no attribute '_Spam_eggs'
