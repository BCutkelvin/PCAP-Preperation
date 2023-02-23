# - - - - - - - SECTION 2: EXCEPTIONS - - - - - - -
# - - - - - - - PCAP-31-03 2.2 - Extend the Python exceptions hierarchy with self -defined exceptions - - - - - - -

# 8)Cleaning Up with Finally
class SomeSelfDefinedExceptionError(Exception):
    test = True
    print(f'This is from the created self-defined exception class: {test}')


try:
    age = -10
    print(f'the age is: {age}')
    if age < 0:
        raise SomeSelfDefinedExceptionError
    yearOfBirth = 2021 - age
    print(f'the year of birth is: {yearOfBirth}')
except SomeSelfDefinedExceptionError as ssdee:
    print(f'this is from the except clause because the self defined exception has been raised: {ssdee}')
