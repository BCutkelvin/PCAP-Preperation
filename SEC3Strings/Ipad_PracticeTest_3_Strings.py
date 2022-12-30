#PCAP PRACTICE TEST 3 EXAM BLOCK #3 STRINGS
#_________________________________________________
#30 which option is true
#NOTE: ord('h') = 104; ord('H') = 72
#print( "not 'hello' is 'Hello':", not 'hello' is 'Hello' )
#print( "'hello' > 'Hello':", 'hello' > 'Hello')
#print("'hello' is 'Hello':", 'hello' is 'Hello')
#print("'hello' <= 'Hello':", 'hello' <= 'Hello')

#32 what is the output of the following code?
s = '0123456789'
#RE: 
#print("s[::2]:", s[::2])
#print("s[:-2:2]:",s[:-2:2])
#print("s[2::2]", s[2::2])
#print(s[::2], s[:-2:2],s[2::2])

#35 which of the calls below are valid String function calls and will return True?
#print("'Abc'.istitle(): ", 'Abc'.istitle())
#print("'123abc'.islower(): ", '123abc'.islower())
#print("'abc'.isalpha(): ",'abc'.isalpha())
#print("'123'.isdigit(): ", '123'.isdigit())
#print("'123abc:'.isidentifier(): ", '123abc'.isidentifier())			#.identifier() is NOT a String method!
#print("'abc123'.isalnum: ", 'abc123'.isalnum() )

#36 what is the output of the following code?
#print("\\\\\")		#SYNTAX ERROR! RE: "\\" should come in pairs; ex "\\\\"

#40 What is the output of the following code?
print("\\//\\//", len ("\\//\\//"))

#42 what will be printed in the following code?
spam = """"""
ham = """
"""
print('spam, ham: ', (spam, ham))
#i two new line charcter                     #WRONG
#ii an empty string and a new line character #CORRECT!!
#iii Syntax Error.                           #WRONG
#iv Two empty strings.                       #WRONG