class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_ones +=1
                max_ones = max(current_ones,max_ones)
            else:
                current_ones = 0
        return max_ones