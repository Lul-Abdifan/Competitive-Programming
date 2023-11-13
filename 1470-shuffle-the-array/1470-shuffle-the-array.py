class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        i = 0
        j = n
        while j < len(nums) and i < n:
            ans +=[nums[i],nums[j]]
            i +=1
            j +=1
        return ans    
        