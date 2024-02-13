class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        cnt = len(nums)/3
        
        ans = [num for num in counter if counter[num] > cnt]
        
        return ans
        