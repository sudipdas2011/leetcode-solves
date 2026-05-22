class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        out = []

        def sfnum(num):
            digits = [int(digit) for digit in str(num)]
            if 0 in (digits):
                return False
            else:
                pass

            return (all(num % digit == 0 for digit in digits))

        for index in range(left, right + 1):
            
            if sfnum(index) == True:
                out.append(index)
            else:
                continue

        return out