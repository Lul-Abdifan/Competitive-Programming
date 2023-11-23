class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        counter = Counter(nums)
        ans_counter = 0
        
        for num in counter:
            ans_counter += min(counter[num],counter[k - num])
        return ans_counter//2
        
        
        