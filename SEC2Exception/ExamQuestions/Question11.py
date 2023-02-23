# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
Question 11: Incorrect
What is the output of the following code?

try:
    raise Exception
except BaseException:
    print("Spam")
except Exception:
    print("Ham")
except:
    print("Eggs")
"""
try:
    raise Exception    # 1st raise Exception occurs...
except BaseException:  # 2nd (lowest) BaseException matches exception...
    print("Spam")      # 3rd print Spam; exit try statement = CORRECT ANSWER!!!
except Exception:
    print("Ham")       # WRONG! NOTE: observe the (highest) Exception class is considered last!
except:
    print("Eggs")      # WRONG!

# Syntax Error         # WRONG!
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
