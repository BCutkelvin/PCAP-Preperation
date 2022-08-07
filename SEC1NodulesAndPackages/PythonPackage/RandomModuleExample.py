# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.3 PGenerate random values using the random module
import random

"""random()"""
print(f'\nrandom.random(): {random.random()}')

"""seed()"""
print(f'\nrandom.seed(10) initialized...')
print(f'random.random() with seed: {random.random()}')

"""choice()"""
aListForChoice = [1, 2, 3, 4, 5]
print(f'\nrandom.choice(aListForChoice): {random.choice(aListForChoice)}')

"""sample()"""
print(f'\nrandom.sample(aListForChoice, k = 2): {random.sample(aListForChoice, k=2)}')
