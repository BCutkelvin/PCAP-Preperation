# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.1 - Import and use modules and packages - - - - - - -

# 3)The import Statement

import mod as someOtherModule

print(f'\nsomeOtherModule.aRegularString = {someOtherModule.aRegularString}')

print(f'\nsomeOtherModule.aRegularMethod() = {someOtherModule.aRegularMethod("test")}')
