# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.1 - Import and use modules and packages - - - - - - -

# 11)Subpackages

import PythonPackage.SubPackage1.mod1
print(f'\nPythonPackage.SubPackage1.mod1.foo() = {PythonPackage.SubPackage1.mod1.foo()}')


from PythonPackage.SubPackage1 import mod2
print(f'\nmod2.bar() = {mod2.bar()}')

from PythonPackage.SubPackage2.mod3 import baz
print(f'\nbaz() = {baz()}')

from PythonPackage.SubPackage2.mod4 import qux as betterName
print(f'\nbetterName() = {betterName()}')







