import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        given_no = math.floor(math.sqrt(c))
        
        left = 0
        right = given_no
        
        while left <= right:
            tmp = left * left + right * right
            if tmp == c:
                return True
            elif tmp > c:
                right -=1
            else:
                left +=1
        return False        
