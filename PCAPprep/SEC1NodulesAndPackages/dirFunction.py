# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.1 - Import and use modules and packages - - - - - - -

# 4)The dir() function
print(f'\ndir() = {dir()}')

testAddingListForDeclaration = [1, 2, 3, 4, 5]
print(f'\ndir() = {dir()}')


class testAddingClassForDeclaration:
    pass


testInstanceVariable = testAddingClassForDeclaration()
print(f'\ndir() = {dir()}')


import mod
print(f'dir() = {dir()}')

print(f'\nmod.aRegularString = {mod.aRegularString}')

print(f'\nmod.aRegularList = {mod.aRegularList}')


from mod import aRegularList, aRegularClass
print(f'\ndir() = {dir()}')

print(f'\nmod.aRegularList = {mod.aRegularList}')

test = mod.aRegularList
print(f'\nmod.aRegularClass = {mod.aRegularClass}')


from mod import aRegularString as string
print(f'\ndir() = {dir()}')

print(f'\nmod.aRegularString = {mod.aRegularString}')
