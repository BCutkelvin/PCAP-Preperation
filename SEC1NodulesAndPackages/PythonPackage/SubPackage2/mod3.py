# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.1 - Import and use modules and packages - - - - - - -

# 10)Importing * From a Packages
def baz():
    print('[mod3] baz()')


class Baz:
    pass


# 11)Subpackages
#ex relative import
#from .. import SubPackage1
#print(f'\nSubPackage1: = {SubPackage1}')
