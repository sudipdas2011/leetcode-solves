class Solution:
    def reverse(self, x: int) -> int:

        num = abs(x)

        reversed_num = int(str(num)[::-1])

        sign = ''

        if x < 0:
            sign = '-'
        else:
            pass

        if sign == '-':
            reversed_num *= (-1)
        else:
            pass

        if (-2**31) <= reversed_num <= ((2**31) - (1)):
            ans = reversed_num
        else:
            ans = 0
        
        return ans