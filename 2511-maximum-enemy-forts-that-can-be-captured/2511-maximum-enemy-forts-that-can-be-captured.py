class Solution:
    def captureForts(self, nums):
        mx = 0
        cur_max = 0
        prev = 0
        flag = False

        for i in range(1, len(nums)):
            if nums[i] == 0 and nums[i - 1] != 0:
                flag = True
                prev = nums[i - 1]

            if nums[i] != 0:
                if nums[i] != prev and flag:
                    mx = max(mx, cur_max)
                flag = False
                cur_max = 0

            if flag:
                cur_max += 1

        return mx
