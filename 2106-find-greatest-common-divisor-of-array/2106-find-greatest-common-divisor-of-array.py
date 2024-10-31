class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        small = sorted_nums[0]
        large = sorted_nums[-1]

        largest_common = 1
        
        for i in range(1,large + 1):
            if small % i == 0 and large % i == 0:
                largest_common = i

        return largest_common
