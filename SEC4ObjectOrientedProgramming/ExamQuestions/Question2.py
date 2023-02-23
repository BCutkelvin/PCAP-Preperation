# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 2: Incorrect
Which of the option(s) below is / are valid given the following code?
"""
class Spam:
    __ham, ham = '__ham', 'ham'

    def __eggs(self):
        pass

    eggs = __eggs

s = Spam()
#<<< INSERT CODE HERE >>>

#i)print(Spam.__name__)            #CORRECT!! "Spam"
#ii)print(s.ham.__name__)          #WRONG! 'str' object has no attribute '__name__'
#iii)print(s._Spam__eggs.__name__) #CORRECT!! "__eggs"
#iv)print(s.eggs.__name__)         #CORRECT!! "__ggs"
#v)print(s._Spam__ham.__name__)    #WRONG! AttributeError: 'str' object has no attribute '__name__'
#vi)print(s.__name__)              #WRONG! AttributeError: 'Spam' object has no attribute '__name__'

"""
*NOTE:
-__name__ is a built-in attribute that prints the name of the class,
 type, function, method, descriptor, or generator instance.
#ex the following code illustrates the use of __name__:

class Bar(object):
    def foo():
      #...
      pass

    print foo.__name__  #foo
print Bar.__name__      #Bar
"""
