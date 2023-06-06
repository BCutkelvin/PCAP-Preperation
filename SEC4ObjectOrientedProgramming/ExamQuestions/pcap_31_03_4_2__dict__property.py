# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - PCEP-31-03 4.2 - Employ class and class and object properties - - - - - - -
""" the __dict__ property (objects vs classes) - - - - - - -"""
#__dict__:
#   -contains dynamic attributes of an object
#   -...stores the attributes of an object
#   -...represents a dictionary or mapping object that is used
#     to store the attributes of the object

# __dict__ is a "mappingproxy object"; can use the dictionary
#   via applying the __dict__property to a class object

# __dict__ is the namespace supporting arbitrary function attributes

#ex. by means of the __dict__ attribute, create a dictionary out of any object:
class Flowers:

    #constructor
    def __init__(self):
        #Keys...
        self.Rose = 'red'
        self.Lily = 'white'
        self.Lotus = 'pink'

    def displayit(self):
        print("\nThe dictionary from object fields belongs to the class Flowers: \t")

#create an instance...
flowers = Flowers()
flowers.displayit()

#calling ATTRIBUTE __dict__...
print(flowers.__dict__) #OUTPUT: {'Rose': 'red', 'Lily': 'white', 'Lotus': 'pink'}

print("\n_____________________________________________________________________________________\n")

#ex. displaying dictionary attributes of a variable and a method using __dict__
def funct():
    pass

funct.practice = 1
print("funct.practice: \t", funct.practice)     #OUTPUT: 1  

class PracticeClass:
    x = 1

    def practice_function(self):
        pass

print("PracticeClass.__dict__\t:", PracticeClass.__dict__)











