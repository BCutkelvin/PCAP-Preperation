# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 3 Strings - - - - - - -
"""
Question 29: Incorrect
Which option will return a different result given the code below?

s = 'Python'        # [0] [1] [2] [3] [4] [5]
                    #  P   y   t   h   o   n
                    #[-6][-5][-4][-3][-2][-1]
"""
s = 'Python'
#- - - - 1)misc./special circumstances- - - -
#copy entire List
#print("s[:]", s[:])
#copy first or last item in List
print("s[-1]", s[-1])
print("s[1]", s[1])

#- - - - 2)[start:stop]- - - -
#"colon right"
#if[-#:], start at #, INCLUSIVE, go all the way RIGHT
#if[#:], start at #, INCLUSIVE, go all the way RIGHT

#ex
#print("s[-2:]", s[-2:]) #on
#print("s[2:]", s[2:])   #thon

#"colon left"
#if[:-#], start at #, EXCLUSIVE, go all the way LEFT
#if[:#], start at #, EXCLUSIVE, go all the way LEFT
#ex
#print("s[:-2]", s[:-2]) #Pyth
#print("s[:2]", s[:2])   #Py
#print("s[-1:3]", s[-1:3])   #empty List

#print(s[-1:-5])        #INVALID! no output cannot traverse left from [-1]
#print(s[-5:-1])        #"ytho"

#- - - - 3)[start:stop:step]- - - -
#ex
print("s[::-1])", s[::-1])         #[::-#]  => ALL ITEMS, REVERSED!
print("s[::-2])", s[::-2])         #[::-#]  => ALL ITEMS, REVERSED!
#print("s[::2])", s[::2])
#print(s[::-2])         #[::-#]  => ALL ITEMS, REVERSED BUT STEP "2" & INCLUSIVE W/START: 0 1 2 3 4 5
                                                                                        #n o h t y P
                                                                                        #|   |   |  , so "nhy"
"""                                                                                        
#print(s[::-3])         #[::-#]  => ALL ITEMS, REVERSED BUT STEP "3" (0 INCLUSIVE W/START: 0 1 2 3 4 5
                                                                                        #n o h t y P
                                                                                        #|      | , so "nt"
#print(s[5::-5])        #[#::-#]  => THE 1ST 2 ITEMS, REVERSED!
#print(s[:-5:-5])       #[:-#:-#] => THE LAST 2 ITEMS, REVERSED!
#print(s[-5::-5])       #[-#::-#] => EVERYTHING EXCEPT THE LAST 2 ITEMS, REVERSED!
"""
# s = 'Python'
# print(s[::-5])         #CORRECT!! "nP";
# print(s[::1][::-5])    #WRONG     "Pn"
# print(s[::5])          #WRONG     "Pn"
# print(s[0]+s[-1])      #WRONG     "Pn"
