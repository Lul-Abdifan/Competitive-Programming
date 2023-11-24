class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l = r = 0
        possible_zeros = 1 
        longest_subarray = 0

        while r < len(nums):
            if nums[r] == 0:
                possible_zeros -= 1

            while possible_zeros < 0:
                if nums[l] == 0:
                    possible_zeros += 1
                l += 1

            longest_subarray = max(longest_subarray, r - l)

            r += 1

        return longest_subarray
