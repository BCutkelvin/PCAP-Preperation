# - - - - - - - SECTION 2: EXCEPTIONS - - - - - - -
# - - - - - - - PCAP-31-03 2.1 - Handle errors using Python-defined exceptions - - - - - - -

# 8)Cleaning Up with Finally
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
    try:
        with open('file.lo') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(f'ERROR! File not!= {fnf_error}')
finally:
    print('Running! don\'t give a damn about any Exceptions!')
