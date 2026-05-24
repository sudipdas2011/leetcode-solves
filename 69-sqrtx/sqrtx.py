import math

class Solution:
    def mySqrt(self, x: int) -> int:
        # Step 1: Handle small edge cases safely
        if x == 0:
            return 0
        if x == 1 or x == 2 or x == 3:
            return 1
            
        # Step 2: Set a smart initial guess using log2
        # For x = 1024, math.log2(1024) is 10
        guess = math.log2(x) 
        
        # Step 3: Loop Newton's Method until convergence
        while True:
            # The standard Newton formula: 0.5 * (guess + x / guess)
            better_guess = 0.5 * (guess + (x / guess))
            
            # If the value stops changing significantly, we found it
            if math.floor(better_guess) == math.floor(guess):
                break
                
            guess = better_guess
            
        return math.floor(guess)
