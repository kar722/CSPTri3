# Hack 2: Write Factorial function using classes, providing implementation of call.
# Print final number

# to run: type "python week2/factorial.py" (without quotes) in the shell

class Factorial:
    def __init__(self):
        self.factoSeq = [1, 1]
    def __call__(self, n):
        if n < len(self.factoSeq):
            return self.factoSeq[n]
        else:
            # Compute the requested Factorial number
            facto_number = n * self(n - 1)
          # two recursive calls to self (__call__(self, n))
            self.factoSeq.append(facto_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.factoSeq[n]
      
facto_of = Factorial() # object instantiation and run __init__ method

n=int(input("Input a number to compute the factiorial : "))
print(facto_of(n)) # object running __call__ method


