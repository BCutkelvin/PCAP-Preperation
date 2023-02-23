# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
What is the output of the following code?

class Spam(Exception):
    pass
class Ham(Spam):
    pass
for cls in [Spam, Ham]:
    try:
        raise cls()
    except Spam:
        print("Spam", end=" ")
    except Ham:
        print("Ham", end=" ")
"""
class Spam(Exception):
    pass
class Ham(Spam):
    pass
for cls in [Spam, Ham]:         #aka for i in [Spam, Ham]...
    try:
        raise cls()             #so raised exception, so...
    except Spam:
        print("Spam", end=" ")
    except Ham:                 #NOTE: (precompile error "'Spam', superclass of the exception class 'Ham',
        print("Ham", end=" ")   # has already been caught"; thus, the raised Spam and Ham exception will both
                                # got to except Spam, since both classes are compatible with Spam
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Spam Ham           WRONG
#Spam Spam          CORRECT!!
#Spam Ham Spam Ham  WRONG
#Invalid Syntax     WRONG