# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 4: Incorrect
Select which option will call the __init__ method of Exception based on the code below.

class SpamException(Exception):
  def __init__(self, message):
    <<< INSERT CODE HERE >>>
    self.message = message
raise SpamException("Spam")W
"""


class SpamException(Exception):
    def __init__(self, message):
        # Exception.__init__(self,message)             #WRONG
        # super(SpamException, self).__init__(message) #CORRECT
        # super.__init__message()                      #WRONG
        super().__init__message()                      #CORRECT
        super(SpamException, self).__init__(message)
        self.message = message


raise SpamException("Spam")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
