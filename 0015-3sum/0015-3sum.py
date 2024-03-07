class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        if len(nums) < 3:
            return []
        
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                
                is_zero = nums[i] + nums[j] + nums[k]
                if is_zero == 0:
                    result.add((nums[i],nums[j],nums[k]))
                    j +=1
                    k -=1
                elif is_zero > 0:
                    k -=1
                else:
                    j +=1
        return result          

            
            
            