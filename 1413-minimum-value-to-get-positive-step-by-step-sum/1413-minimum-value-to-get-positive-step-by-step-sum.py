class Solution:
    def minStartValue(self, nums: List[int]) -> int:
      
        minimum_sum =  nums[0] if nums[0] < 1 else float('inf') 

        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i - 1]
            if minimum_sum > nums[i]:
                minimum_sum = nums[i]
        value = 1 + abs(minimum_sum) if minimum_sum < 0  else 1
        return value

           
            
            
            
        
        