# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.1 - Import and use modules and packages - - - - - - -

# 3)The import Statement
"""
you could call attributes from file module (mod) import in this manner:
import mod

print(f'\nmod = {mod}')

print(f'\nmod.aRegularString = {mod.aRegularString}')

print(f'\nmod.aRegularMethod() = {mod.aRegularMethod("test")}')

but the better alternate form would is "from...import..." instead:
"""
from mod import aRegularString, aRegularList, aRegularMethod, aRegularClass

print(f'\naRegularString = {aRegularString}')

print(f'\naRegularList = {aRegularList}')

print(f'\naRegularMethod = {aRegularMethod}')  # will display "hex" object from symbol table
print(f'\nmod.aRegularMethod() = {aRegularMethod("test")}')

print(f'\naRegularClass = {aRegularClass}')    # will display "hex" object from symbol table

anInstance = aRegularClass()
print(f'\naRegularClass = {anInstance}')       # will display "hex" object from symbol table
