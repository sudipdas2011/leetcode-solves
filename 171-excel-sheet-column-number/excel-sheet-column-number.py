class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        alpha = {
            letter: i for i, letter in enumerate(string.ascii_uppercase, 1)
        }

        t = list(columnTitle)
        t.reverse()

        length = len(t)

        answer = 0

        for i in range(length):
            answer += (alpha[(t[i])]) * (26**i)
        
        return answer