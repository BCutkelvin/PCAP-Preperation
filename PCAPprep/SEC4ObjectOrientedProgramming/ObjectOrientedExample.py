# - - - - - - - SECTION 4: OBJECT-ORIENTED PROGRAMMING - - - - - - -
# - - - - - - - PCAP-31-03 4.1 - Understand the Object-Oriented Approach
# - - - - - - - PCAP-31-03 4.2 - Employ class and object properties
# - - - - - - - PCAP-31-03 4.3 - Equip a class with methods
# - - - - - - - PCAP-31-03 4.4 - Discover the class structure
# - - - - - - - PCAP-31-03 4.5 - Build a class hierarchy using inheritance
# - - - - - - - PCAP-31-03 4.6 - Construct and initialize objects

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} old'

    def description(self):
        return f'{self.name} is {self.age} old'

    def speak(self, sound):
        return f'{self.name} says {sound}'


dogInstance1 = Dog("Buddy", 9)
dogInstance2 = Dog("Miles", 4)

print(f'\ndogInstance1.species: {dogInstance1.species}')
print(f'dogInstance2.species: {dogInstance2.species}')

print(f'\ndogInstance1.name: {dogInstance1.name}')
print(f'dogInstance1.age: {dogInstance1.age}')

print(f'\ndogInstance2.name: {dogInstance2.name}')
print(f'dogInstance2.age: {dogInstance2.age}')

print(f'\ndogInstance1.description(): {dogInstance1.description()}')
print(f'dogInstance2.description(): {dogInstance2.description()}')
print(f'dogInstance1.__str__(): {dogInstance1.__str__()}')

print(f'\ndogInstance1.speak: {dogInstance1.speak("woof woof!")}')
print(f'dogInstance2.speak: {dogInstance2.speak("bow wow")}')


class Bulldog(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

bulldogInstance = Bulldog("Jack", 3)

print(f'\nbulldogInstance.species: {bulldogInstance.species}')
print(f'bulldogInstance.name: {bulldogInstance.name}')
print(f'bulldogInstance.age: {bulldogInstance.age}')

print(f'\ntype(bulldogInstance): {type(bulldogInstance)}')
print(f'isinstance(bulldogInstance, Dog): {isinstance(bulldogInstance, Dog)}')

print(f'\nbulldogInstance.speak(): {bulldogInstance.speak()}')



