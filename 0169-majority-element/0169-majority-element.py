class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elt = None
        cnt = 0
        
        
        for num in nums:
            if cnt == 0:
                elt = num
                cnt +=1
            elif num != elt:
                cnt -=1
            else:
                cnt +=1
        return elt        
                
                
                
        
        