class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = 0
        left_sum = 0
        n =len(nums)
        
        
        for i in range(n):
            total_sum +=nums[i]
          
        for i in range(n):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]  
            
        return -1   