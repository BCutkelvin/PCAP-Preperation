# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 36: Incorrect
Which option(s) are valid replacements for the marked section below.
"""


class Bar:
    def __init__(self):
        self.x = 1


class Foo(Bar):
    def __init__(self):
        super(Spam, self).__init__()
        self.y = 2


f = Foo()
print(f.x, f.y)

# i)super(Spam, self).__init__()                                            #CORRECT!!
# ii)None. All results in AttributeError:'Foo' object has no attribute 'x'  #WRONG!
# iii)Blank. code will work without replacement         `                   #WRONG!
# iv)Bar.__init__ (self)                                                    #CORRECT!!
