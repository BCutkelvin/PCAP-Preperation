# - - - - - - - SECTION 2: EXCEPTIONS - - - - - - -
# - - - - - - - PCAP-31-03 2.1 - Handle errors using Python-defined exceptions - - - - - - -

# 2)Raising an Exception

someAge = 47
if someAge > 46:
    raise Exception(f'someAge should not exceed: {someAge}')
