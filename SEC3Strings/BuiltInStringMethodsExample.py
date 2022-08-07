# - - - - - - - SECTION 3: STRINGS - - - - - - -
# - - - - - - - PCAP-31-03 3.3 - Employ built - in string methods

# 3) Find and Replace

someStringWithLength = "I'm just a plain ole plain ole string"
"""
print(f'\nsomeStringWithLength.count("plain"): {someStringWithLength.count("plain")}')

print(f'\nsomeStringWithLength.find("ole"): {someStringWithLength.count("ole")}')
print('someStringWithLength.find("plain"): {someStringWithLength.count("plain", 12)}')

print(f'\nsomeStringWithLength.rfind("ole"): {someStringWithLength.count("ole")}')

print(f'\nsomeStringWithLength.rindex("ole"): {someStringWithLength.index("plain")}')

print(f'\n')
print(' '.join(someStringWithLength))

print(f'\n')
print(someStringWithLength.split(' '))
"""
someListOfRandomNumbers = ['8', '4', '7', '6', '46']
print(f'\nsorted(someListOfRandomNumbers): {sorted(someListOfRandomNumbers)}')

someStringOfRandomNumbers = '847646'
print(f'sorted(someStringOfRandomNumbers): {sorted(someStringOfRandomNumbers)}')
print(f'sorted(someStringWithLength): {sorted(someStringWithLength)}')

someListOfCaseSensitiveNames = ['Mike', 'raph', 'don', 'Leo']
print(f'\nsorted(someListOfCaseSensitiveNames): {sorted(someListOfCaseSensitiveNames)}')
print(f'sorted(someListOfCaseSensitiveNames, key = len): {sorted(someListOfCaseSensitiveNames, key = len)}')
print(f'sorted(someListOfCaseSensitiveNames, key = str.lower): {sorted(someListOfCaseSensitiveNames, key = str.lower)}')

print(f'\nsomeListOfRandomNumbers = :{someListOfRandomNumbers}')
print(f'someListOfRandomNumbers.sort(): {someListOfRandomNumbers.sort()}')
print(f'someListOfRandomNumbers after sort(): {someListOfRandomNumbers}')





