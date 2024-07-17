class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_index = furthest_index = 0

        for current_index in range(len(nums)):
            furthest_index = max(furthest_index, current_index + nums[current_index])
            if furthest_index >= len(nums) - 1:
                return True
            elif current_index >= furthest_index:
                return False
        
        return True
