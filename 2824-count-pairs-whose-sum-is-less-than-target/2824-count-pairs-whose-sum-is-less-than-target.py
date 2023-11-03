class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        counter = 0
        i,j = 0,len(nums) - 1
        while(i < j):
            if nums[i] + nums[j] < target:
                counter +=j - i
                i +=1
            else:
                j -=1
        return counter 

 