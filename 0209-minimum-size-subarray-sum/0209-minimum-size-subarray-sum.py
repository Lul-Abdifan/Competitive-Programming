class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        current_sum = 0
        j = 0
        
        for i in range(len(nums)):
            current_sum +=nums[i]
            
            while(current_sum >=target):
                min_length = min(min_length,i-j + 1)
                current_sum -=nums[j]
                j+=1
            
        return 0 if min_length == float('inf') else min_length      
                
                
                
        