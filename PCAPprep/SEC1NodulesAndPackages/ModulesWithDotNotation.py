# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.1 - Import and use modules and packages - - - - - - -
# 8)Python Packages
import SEC1NodulesAndPackages

SEC1NodulesAndPackages.mod1.foo()
print(f'\nPythonPackage.mod1.foo() = {SEC1NodulesAndPackages.mod1.foo()}')

x = SEC1NodulesAndPackages.mod2.Bar()
print(f'\nx = PythonPackage.mod2.Bar() = {x}')

"""
can also access using other import syntax forms:
from PythonPackage.mod1 import foo

from PythonPackage.mod1 import Bar as AnAlternateName

from PythonPackage import mod1

from PythonPackage import mod1 as variable
...
variable.bar() 
"""
