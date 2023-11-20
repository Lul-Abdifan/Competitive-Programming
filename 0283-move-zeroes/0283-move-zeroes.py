class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
         l = 0
         r = 0
         n = len(nums)

         while r < n: 
            if nums[l] == 0 and nums[r] != 0: 
                
                nums[l] = nums[r]
                nums[r] = 0
                l +=1
            
            if  nums[l] != 0:
                l +=1
            
            r +=1
                
            
        
        