class Solution:
    def isHappy(self, n: int) -> bool:
        
        listn = [] #list of digits of current n
        proxyn = n #sum of the digits squared to be used to set n again
        listhappies = [] #list of 'n's for repetition check
        hasdup = False #boolean for duplicates of 'n' in 'listhappies'

        if n <= 0:
            answer = False
        else:
            while n != 1 and hasdup == False:
                listn = [int(d) for d in str(n)]
                proxyn = sum(x**2 for x in listn)
                listhappies.append(proxyn)
                hasdup = len(listhappies) != len(set(listhappies))
                n = proxyn #new n for nect iteration
            #two conditions n == 1 or hasdup == True
            else:
                if n == 1:
                    answer = True
                elif hasdup == True:
                    answer = False
                else:
                    pass

        return answer