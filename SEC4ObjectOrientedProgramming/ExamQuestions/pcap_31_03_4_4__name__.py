# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - PCEP-31-03 4.2 - Employ class and class and object properties - - - - - - -
""" - - - - - - - properties: __name__- - - - - - - """
#

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