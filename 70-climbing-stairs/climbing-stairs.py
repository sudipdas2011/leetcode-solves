import math

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = round((1 / 5**0.5) * (((1 + 5**0.5) / 2)**(n + 1) - (((1 - 5**0.5) / 2)**(n + 1))))
        return ans