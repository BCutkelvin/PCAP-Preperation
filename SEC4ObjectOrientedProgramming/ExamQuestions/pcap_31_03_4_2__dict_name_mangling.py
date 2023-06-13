# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - PCEP-31-03 4.2 - Employ class and class and object properties - - - - - - -
""" - - - - - - - name mangling - - - - - - - """
#-name mangling of private variables, is when every member with a double underscore will be changed to:
#   _object._class_variable
#   so it can still be accessed from outside the class
#-practice should be refrained from!
#-name mangling means there is limited support of a valid use-case for class-private members to avoid name clashes of
# names defined by subclasses
#-name mangling rules are designed to mostly avoid accidents, but it is still possible to access or modify a variable
# that is considered private. this can even be useful in special circumstances, such as in the debugger

#ex. an identifier of the form __geek is replaced with _classname__geek, where classname is the current class name with
# leading underscore(s) stripped; observe how the underscore works
class Map:
    def __init__(self, iterate):
        self.list = []
        self.__geek(iterate)

    def geek(self, iterate):
        for item in iterate:
            self.list.append(item)

    #private copy of original geek() method
    __geek = geek

class MapSubclass(Map):
    #provides new signature for geek() but does not break __init__()
    def geek(self, key, value):
        for i in zip(key, value):
            self.list.append(i) ,