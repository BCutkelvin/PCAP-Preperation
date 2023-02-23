# - - - - - - - SECTION 3: STRINGS - - - - - - -
# - - - - - - - PCAP-31-03 3.1 - Understand machine representation of characters - - - - - - -

# 2)The String module

whitespace = ' \t\n\r\v\f'
print(f'\nwhitespace: {whitespace}')

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
print(f'ascii_lowercase: {ascii_lowercase}')

ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(f'ascii_uppercase: {ascii_uppercase}')

ascii_letters = ascii_lowercase + ascii_uppercase
print(f'ascii_letters: {ascii_letters}')

digits = '0123456789'
print(f'digits: {digits}')

hexdigits = digits + 'abcdef' + 'ABCDEF'
print(f'hexdigits: {hexdigits}')

octdigits = '01234567'
print(f'octdigits: {octdigits}')

punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
print(f'punctuation: {punctuation}')

printable = digits + ascii_letters + punctuation + whitespace
print(f'printable: {printable}')
