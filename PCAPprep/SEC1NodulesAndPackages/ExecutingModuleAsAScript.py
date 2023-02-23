# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.1 - Import and use modules and packages - - - - - - -

# 5)Python Modules: Executing a Module as a Script

aRegularString = "If God says it, must be right it!"

aRegularList = [100, 200, 300]


def aRegularMethod(arg):
    print(f'\narg = {arg}')


class aRegularClass:
    pass


if __name__ == '__main__':
    print("executing as a standalone script:\n")
    print(f'\naRegularString = {aRegularString}')
    print(f'\naRegularList = {aRegularList}')
    print(f'\nmod.aRegularMethod() = {aRegularMethod("test")}')
    anInstance = aRegularClass()
    print(f'\naRegularClass = {anInstance}')
