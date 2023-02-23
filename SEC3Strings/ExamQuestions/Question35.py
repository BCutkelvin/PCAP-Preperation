# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 3 Strings - - - - - - -
"""
Question #35: INCORRECT
which of the calls below are valid String function calls and will return True?
"""
#i)'Abc'.istitle()          #CORRECT!!
#ii)'123abc'.islower()      #CORRECT!!
#iii)'abc'.isalpha()        #CORRECT!!
#iv)'123'.isdigit()         #CORRECT!!
#v)'123abc:'.isidentifier() #WRONG!
#vI)'abc123'.isalnum        #CORRECT!!

print("'Abc'.istitle(): ", 'Abc'.istitle())
print("'123abc'.islower(): ", '123abc'.islower())
print("'abc'.isalpha(): ",'abc'.isalpha())
print("'123'.isdigit(): ", '123'.isdigit())
print("'123abc:'.isidentifier(): ", '123abc'.isidentifier())			#.identifier() is NOT a String method!
print("'abc123'.isalnum: ", 'abc123'.isalnum() )


