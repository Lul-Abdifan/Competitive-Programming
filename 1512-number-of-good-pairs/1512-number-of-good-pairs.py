class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        no_pairs = 0
        
        for cnt in counter:
            if counter[cnt] > 1:
                no_pairs += (counter[cnt] * (counter[cnt] - 1))//2
        return no_pairs     
