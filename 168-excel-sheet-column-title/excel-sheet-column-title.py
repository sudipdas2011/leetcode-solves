import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        alpha = {i: letter for i, letter in enumerate(string.ascii_uppercase, 1)}
        answer_list = []
        r = 1
        n = columnNumber

        while n > 0:
            r = n % 26

            if r == 0:
                r = 26

            n -= r
            n //= 26

            answer_list.append(alpha[r])
        else:
            pass

        answer_list.reverse()
        result = "".join(answer_list)

        return result