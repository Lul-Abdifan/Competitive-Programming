class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        max_ones = float('-inf')
        while r < len(nums):
            if nums[r] == 1:
                r +=1
                
            elif r < len(nums) and nums[r] == 0 and k >= 1:
                 k -=1
                 r +=1   
            else:
                max_ones = max(max_ones,r - l)    
                while k <= 0:
                    if nums[l] == 0:
                        k +=1
                    l +=1 
            max_ones = max(max_ones,r - l)         
                
        return max_ones 
                    
                 
               
                   
         