class Solution:
    def addDigits(self, num: int) -> int:

        proxynum = 99
        length = len(str(proxynum))
        listnum = []

        while length != 1:
            listnum = [int(digit) for digit in str(num)]
            proxynum = sum(listnum)
            length = len(str(proxynum))
            num = proxynum
        else:
            ans = num
        
        return ans
        