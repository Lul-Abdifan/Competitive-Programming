class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
         if k <= 1:
                return 0
         
         left = 0
         no_counter = 0
         products = 1
            
         for right in range(len(nums)):
            products *=nums[right]
            
            while products >= k:
                products /=nums[left]
                left +=1
            
            no_counter += right - left + 1
            
            
            
            
            
         return no_counter   
        