class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        numOfZero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numOfZero+=1
                continue
            else:
                prod *=nums[i]

        for i in range(len(nums)):
             if numOfZero == 0:
                 nums[i] = int(prod/nums[i])

             elif numOfZero==1 and nums[i]==0:
                  nums[i] = prod
             else:
                  nums[i] = 0
             
        return nums
                  
                       
                       
                       
                       
                 

                    
                    
        