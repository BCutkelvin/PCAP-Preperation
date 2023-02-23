# - - - - - - - SECTION 2: EXCEPTIONS - - - - - - -
# - - - - - - - PCAP-31-03 2.1 - Handle errors using Python-defined exceptions - - - - - - -

# 5)Catching Exceptions with try and except
import sys


def linux_interaction():
    assert ('linux' in sys.platform), "\nFunction can only run on Linux systems."
    print(f'Doing something.')


try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print("\nthe linux_interaction() function was not executed")
