# Hack 4: Extra Credit. Write Palindrome function using classes, providing implementation of call.

import re


class Palindrome:
    # palindrome initializer method
    def __init__(self, candidate):
      # input values
      self._candidate = candidate  # input string
      self._length = len(candidate)  # input length
      # analysis values 
      self._is_a_palindrome = False  # initialize status
    
      self._az09 = re.sub(r'[^a-zA-Z0-9]', '', self._candidate)  # alpha numeric characters
 
      self._analysis = []  # array of tests
      self._tests = 0  # counter of tests performed
      # evaluate for palindrome
  
      self.__call__()  

    # palindrome tester method
    def __call__(self):
      c = self._az09
      # Run loop from 0 to len/2 of string (middle is exit point)
      tests = int(len(c) / 2)
    
      for i in range(0, tests):
          front = c[i];
          back = c[len(c) - i - 1]
          if front.lower() == back.lower():
              self.logger(front, back, True)
              self._tests += 1
          else:
              self.logger(front, back, False)
              return
      self._is_a_palindrome = True
      return

    # palindrome logging
    def logger(self, front, back, result):
      self._analysis.append({"test": self._tests, "front": front, "back": back, "result": result})

      
# Tester Code
def pal():      
  good = "tattarrattat"
  goodphrase = "A man, a plan, a canal -- Panama!"
  bad = "onomatopoeia"
  badphrase = "ThE tInY mOu4e wSA 5eaDi8g"
  
  Entry1 = Palindrome(good)
  Entry2 = Palindrome(goodphrase)
  Entry3 = Palindrome(bad)
  Entry4 = Palindrome(badphrase)
  
  # access the class attributes
  print(f"{good} is {Entry1._is_a_palindrome}")
  print(f"{bad} is {Entry3._is_a_palindrome}")
  print(f"{goodphrase} is {Entry2._is_a_palindrome}")
  print(f"{badphrase} is {Entry4._is_a_palindrome}")

if __name__ == "__main__":
    pal()