class mathFunc:
  def __init__(self,firstnumber,secondnumber):
    self.firstnumber=firstnumber
    self.secondnumber=secondnumber
    
  def findlcm(self):
      if (self.firstnumber > self.secondnumber):
          maximum = self.firstnumber
      else:
          maximum = self.secondnumber
      while (True):
          if (maximum % self.firstnumber == 0 and maximum % self.secondnumber == 0):
              break
          maximum = maximum + 1
      return maximum

  def __call__(self):
    ans = self.findlcm()
    print("\n Least Common Multiple of {0} and {1} is: {2}".format(self.firstnumber, self.secondnumber, ans))
    print()

def printmath():
    math = mathFunc(23,10013)
    math()

if __name__ == "__main__":
  printmath()

