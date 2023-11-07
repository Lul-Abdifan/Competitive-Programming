class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        num = [0] * len(nums) 
        while i <= j:
            if abs(nums[i]) >= nums[j]:
                num[k] = nums[i] * nums[i]
                i += 1
            else:
                num[k] = nums[j] * nums[j]
                j -= 1
            k -= 1

        return num
