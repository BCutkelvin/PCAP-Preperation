# - - - - - - - SECTION 3: STRINGS - - - - - - -
# - - - - - - - PCAP-31-03 3.1 - Understand machine representation of characters - - - - - - -

# 2)The String module

import string

s = "What's wrong with ASCII?!?!?!"
print('s.rstrip(string.punctuation): ', s.rstrip(string.punctuation))
