class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = 0
        zeros_count = 1
        max_count = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count -=1
                
            while zeros_count < 0:
                if nums[left] == 0:
                    zeros_count +=1
                left +=1
            max_count = max(max_count,right - left)
        return max_count    
                
                        
        
  
        