# - - - - - - - SECTION 3: STRINGS - - - - - - -
# - - - - - - - PCAP-31-03 3.2 - Operations On Strings

# 4)String Indexing

someStringWithLength = "I'm just a plain ole string"

print(f'\nsomeStringWithLength[0] = {someStringWithLength[0]}')
print(f'someStringWithLength[10] = {someStringWithLength[10]}')
print(f'someStringWithLength[25] = {someStringWithLength[25]}')
print(f'len(someStringWithLength) = {len(someStringWithLength)}')
print(f'len(someStringWithLength) - 1 = {len(someStringWithLength) - 1}')

print(f'\nsomeStringWithLength[-1] = {someStringWithLength[-1]}')
print(f'someStringWithLength[-11] = {someStringWithLength[-11]}')
print(f'someStringWithLength[-26] = {someStringWithLength[-26]}')

print(f'\nsomeStringWithLength[0:10] = {someStringWithLength[0:10]}')
print(f'someStringWithLength[10:25] = {someStringWithLength[10:25]}')

print(f'\nsomeStringWithLength[:15] = {someStringWithLength[:15]}')
print(f'someStringWithLength[0:15] = {someStringWithLength[0:15]}')

print(f'\nsomeStringWithLength[10:] = {someStringWithLength[10:]}')
print(f'someStringWithLength[10:len(someStringWithLength)] = {someStringWithLength[10:len(someStringWithLength)]}')

print(f'\nsomeStringWithLength[:] = {someStringWithLength[:]}')

print(f'\nsomeStringWithLength[5:5] = {someStringWithLength[5:5]}')
print(f'someStringWithLength[15:5] = {someStringWithLength[15:5]}')

# re: "I'm just a plain ole string"
print(f'\nsomeStringWithLength[0:25:1] = {someStringWithLength[1:25:2]}')
