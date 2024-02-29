class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        no_zeros = 0
        no_ones = 0
        no_twos = 0
        
        for num in nums:
            if num == 0:
                no_zeros +=1
            elif num == 1:
                no_ones +=1
            else:
                no_twos +=1
                
                
        for i in range(len(nums)):
            if no_zeros > 0:
                nums[i] = 0
                no_zeros -=1
                
            elif no_ones > 0: 
                nums[i] = 1
                no_ones -=1
            else:
                nums[i] = 2
                
            
            
        
        
                
                
                
                
        