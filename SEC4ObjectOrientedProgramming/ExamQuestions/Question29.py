# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 29: Incorrect
Which of the statements below is valid?
"""


class A:
    def __init__(self):
        pass

    def spam(self):
        pass

    def ham(self):
        return o.ham()


a = A()

o.ham()


# i)Replace <CALL spam> with self.spam(self)    #WRONG: Unresolved reference 'self'
# ii)Replace <CALL ham> with a.ham(a)           #CORRECT!
# iii)Replace <CALL spam> with self.spam()      #WRONG: Unresolved reference 'self'
# iv)Replace <CALL ham> with o.ham()            #WRONG: Unresolved reference 'o'
