class Solution:
    def minSwaps(self, s: str) -> int:
        ones = 0
        zeros = 0

        odd_one = 0
        even_one = 0
        odd_zero = 0
        even_zero = 0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=='0':
                    even_zero+=1
                else:
                    even_one+=1
            else:
                if s[i]=='0':
                    odd_zero+=1
                else:
                    odd_one+=1

            if s[i]=='0':
                zeros += 1
            else:
                ones += 1
        if abs(ones - zeros) > 1: return -1

        if ones==zeros:
            if odd_one >= even_one:
                return even_one
            else:
                return odd_one
        elif ones > zeros:
            return odd_one
        else:
            return odd_zero