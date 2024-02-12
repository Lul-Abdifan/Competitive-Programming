class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        tmp_nums = [0]*n
    
        i = 0
        j = 1
            
        for num in nums:
            if i < len(nums) - 1 or j < len(nums):
                if num > 0:
                   tmp_nums[i] = num
                   i +=2
                
                else:
                   tmp_nums[j] = num
                   j +=2
        return tmp_nums        

            
        
        
                
                
            
            
                
            
        