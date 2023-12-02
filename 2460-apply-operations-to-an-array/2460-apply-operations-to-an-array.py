class Solution:
    def move_zeros(self,nums:List[int]):
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l] = nums[r]
                l +=1
            r +=1
        while l < len(nums):
            nums[l] = 0
            l +=1
    def applyOperations(self, nums: List[int]) -> List[int]:
        
       
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *=2
                nums[i + 1] = 0
        j = 0
        self.move_zeros(nums)
        
            
       
                
        return nums   
    
               
                
        