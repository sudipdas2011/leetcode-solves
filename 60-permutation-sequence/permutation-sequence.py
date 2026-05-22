import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Step 1: Make a list of numbers we can use
        # Example for n=3: ['1', '2', '3']
        numbers = []
        for i in range(1, n + 1):
            numbers.append(str(i))
            
        # Step 2: Change k to 0-based index to make math easier
        # If k=3, it becomes index 2 (0, 1, 2 -> 3rd item)
        k = k - 1
        
        result = ""
        
        # Step 3: Find digits one by one from left to right
        for i in range(n, 0, -1):
            # How many items are in each group?
            # If 3 numbers are left, each group size is (3-1)! = 2
            group_size = math.factorial(i - 1)
            
            # Which group index do we need?
            # Basic division: if k=2 and group_size=2, then 2 // 2 = 1
            group_index = k // group_size
            
            # Pick the number at that index and add it to our answer
            chosen_number = numbers[group_index]
            result = result + chosen_number
            
            # Remove it from available numbers so we don't reuse it
            numbers.remove(chosen_number)
            
            # Find the new position inside the chosen group using remainder
            # 2 % 2 = 0 (we want the first item inside that group)
            k = k % group_size
            
        return result
