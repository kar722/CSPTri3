# Hack 3: Select your own Math function. Write it in Imperative and OOP form. Some Math functions have been provided. Think about inputs and outputs to present to Teacher. It is preferred to have Test data, not input to illustrate code.

# Triangular Numbers
# The numbers in a sequence are referred to as terms. The terms of a triangular sequence are related to the number of dots needed to create a triangle. You would begin forming a triangle with three dots; one on top and two on bottom. The next row would have three dots, making a total of six dots. The next row in the triangle would have four dots, making a total of 10 dots. The following row would have five dots, for a total of 15 dots. Therefore, a triangular sequence begins: “1, 3, 6, 10, 15…”)

# to run: type "python week2/mathfunc.py" (without quotes) in the shell

class Triangular:
    def __init__(self):
        self.triSeq = [0, 1]
    def __call__(self, n):
        if n < len(self.triSeq):
            return self.triSeq[n]
        else:
            # Compute the requested Factorial number
            triangularNumber = self(n-1)+n 
          
          # two recursive calls to self (__call__(self, n))
            self.triSeq.append(triangularNumber) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.triSeq[n]
      
tri_of = Triangular() # object instantiation and run __init__ method

n=int(input("Enter a Number (nth term of Triangular Number Sequence) : "))
print(tri_of(n)) # object running __call__ method

