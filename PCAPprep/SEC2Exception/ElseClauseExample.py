# - - - - - - - SECTION 2: EXCEPTIONS - - - - - - -
# - - - - - - - PCAP-31-03 2.1 - Handle errors using Python-defined exceptions - - - - - - -

# 6)The else clause
import sys


def linux_interaction():
    assert ('linux' not in sys.platform), "\nFunction can only run on Linux systems."
    print('\nDoing linux_interaction()...')


try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print("\nthe linux_interaction() function was not executed")
else:
    print("Executing the else clause because there was no Exception!")
