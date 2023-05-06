# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 39: Incorrect
What is the output of the following code?
"""


class Ham:
    def __init__(self):
        print(type(self).__name__ + '.__init__()', end=' ')
        self.update()  # error occur here! only 1 argument called

    def update(self):
        print(type(self).__name__ + '.update()', end=' ')

    # def update(self, param):
    #    print(type(self).__name__ + '.update(param)', end=' ')


Ham()
print("***DEBUG: help(Ham.update), ", help(Ham.update))

# i)TypeError: update() missing 1 required positional argument 'param'      #CORRECT!!
# ii)Ham.__init()__() Ham.update(param)                                     #WRONG
# iii)Ham.i__init__() Ham.update()                                          #WRONG
# iv)syntaxError: invalid syntax                                            #WRONG

# *NOTE:
# if there were no compile time errors, observe:
#    def update(self):
#         print(type(self).__name__ + '.update()', end=' ')
#   ...
#   OUTPUT:
#   Ham.__init__() Ham.update()
