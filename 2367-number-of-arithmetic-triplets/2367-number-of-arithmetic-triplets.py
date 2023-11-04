class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums.sort()  # Sort the input list in ascending order.
        counter = 0
        n = len(nums)
        for i in range(n - 2):
            x = nums[i]
            j = i + 1
            k = j + 1
            while k < n:
                if nums[j] - x == diff and nums[k] - nums[j] == diff:
                    counter +=1
                    j +=1
                    k +=1
                elif nums[k] - nums[j] > diff and j < k:
                    j +=1
                else:
                    k +=1
                
        return counter
