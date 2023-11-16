class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        less = float('inf')
        less_more = float('inf')

        if len(nums) < 3:
            return False
            
        for num in nums:
            if num <= less:
                less = num
            elif num <= less_more:
                less_more = num   
            else:
                return True
        return False    
    
    
            
        