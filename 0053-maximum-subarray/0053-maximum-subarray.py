class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        maximum_sum = -math.inf
        
        for i in range(len(nums)):
            current_sum +=nums[i]
            
            if current_sum > maximum_sum:
               maximum_sum = current_sum
        
            if current_sum < 0:
               current_sum = 0
        return maximum_sum    
            
            
            
            
        