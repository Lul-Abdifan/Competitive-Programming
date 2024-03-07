class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = set()
        nums.sort()
        
        if len(nums) < 4:
            return []
        
        for i in range(len(nums) - 3):
            for j in range(i + 1,len(nums) - 2):
                k = j + 1
                l = len(nums) - 1
                
                while k < l:
                    tmp_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if tmp_sum == target:
                        result.add((nums[i],nums[j],nums[k],nums[l]))
                        k +=1
                        l -=1
                    elif tmp_sum > target:
                        l -=1
                    else:
                        k +=1
        return result                
                        
                        
                    
        