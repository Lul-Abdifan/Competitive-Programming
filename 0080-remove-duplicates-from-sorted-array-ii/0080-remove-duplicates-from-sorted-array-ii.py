class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        counter = 1

        while right < len(nums):
            if nums[left] != nums[right]:
                counter = 1
                left +=1

                nums[left] = nums[right]
                right +=1

            elif  nums[left] == nums[right] and counter == 1:
                left +=1
                nums[left] = nums[right]
                right +=1
                counter = 2
            else:
                right +=1
        return left + 1        




            
            
            
            
    
    
        
        
        
        
        
        