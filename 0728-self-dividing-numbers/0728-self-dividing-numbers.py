class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right + 1):
            s = i
            self_dividing_no = True
            while s > 0:
                digit = s%10
                if digit == 0 or i%digit != 0:
                    self_dividing_no = False
                    break
                s //=10
            if self_dividing_no:
                ans.append(i)
        return ans        
        