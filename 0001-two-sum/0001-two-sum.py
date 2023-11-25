class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for i in range(len(nums)):
            next_target = target - nums[i]
            if next_target in dict_:
                return [dict_[next_target],i]
            else:
                dict_[nums[i]] = i
          
                
        