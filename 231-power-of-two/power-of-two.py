class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        binary = bin(n)[3:]
        ans = False

        if binary.strip('0'):
            ans = False
        else:
            if n == 0:
                ans = False
            else:
                ans = True

        return ans