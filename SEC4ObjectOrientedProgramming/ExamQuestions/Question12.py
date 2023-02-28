# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 12: Incorrect
    Select the choices which will return TRUE?
"""
class Spam:
  ham = 36

spam = Spam()

#i)print("hasattr(spam, 'ham') :", hasattr(spam, 'ham') )          #CORRECT!!
#ii)print("spam.hasattr('ham') :", spam.hasattr('ham') )           #WRONG
#iii)print("hasattr(pam, 'ham') :", hasattr(pam, 'ham') )          #CORRECT!!
#iv)print("hasattr('spam', 'ham') :", hasattr('spam', 'ham') )     #WRONG
#v)print("hasattr('Spam', 'ham') :", hasattr('Spam', 'ham') )      #WRONG

#RE: hasattr(objet, name), where the argurments are an OBJECT and a STRING