# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.1 - Import and use modules and packages - - - - - - -

# 6)Reloading a Module

import mod

a = [100, 200, 300]
mod.aRegularMethod(a)

import mod

import importlib
importlib.reload(mod)
a = [100, 200, 300]
