# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 27: Incorrect
What is the output of the following code?

class E(Exception):
    def __init__(self, message="Stop"):
        self.message = message
    def __str__(self):
        return "Surprise"

try:
    raise Exception
except E as e:
    print(e)
else:
    print("Goodbye")
"""
class E(Exception):
    def __init__(self, message="Stop"):
        self.message = message

    def __str__(self):
        return "Surprise"

try:
    raise Exception     #OUTPUT: "Exception"; NOTE: this will raise Exception not E! i.e. "Exception"
except E as e:          #THIS DOES NOT MATCH! ("Exception"); thus it is an Unhandled Exception
    print(e)
else:                   #THIS WILL NOT EXECUTE; Exception was raised
    print("Goodbye")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Surprise               #WRONG!
#Goodbye                #WRONG!
#Unhandled Exception    #CORRECT!
#Stop                   #WRONG!
