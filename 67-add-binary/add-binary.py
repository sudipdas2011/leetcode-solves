class Solution:
    def addBinary(self, a: str, b: str) -> str:

        #binary to number
        #a
        a_len = len(str(a))
        a_num = 0
        a_list = [int(d) for d in str(a)]
        a_list.reverse()
        for i in range(a_len):
            a_num += a_list[i] * (2**(i))
        #b
        b_len = len(str(b))
        b_num = 0
        b_list = [int(d) for d in str(b)]
        b_list.reverse()
        for i in range(b_len):
            b_num += b_list[i] * (2**(i))

        #sum
        sum_num = a_num + b_num

        #sum to binary
        q = 1
        r = [] #to return
        while q != 0:
            q = ( sum_num // 2 )
            r.append( sum_num % 2 )
            sum_num = q
        else:
            r.reverse()
            result = "".join(str(x) for x in r)

        return result
