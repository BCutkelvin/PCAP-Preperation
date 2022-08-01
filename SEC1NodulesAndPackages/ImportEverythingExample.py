# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.1 - Import and use modules and packages - - - - - - -

# 3)The import Statement
"""
WARNING ! This is dangerous! (bad practice) it enters names into local symbol table  "in mass"!
"""
from mod import *

print(f'\naRegularString = {aRegularString}')

print(f'\naRegularMethod() = {aRegularMethod("test")}')
