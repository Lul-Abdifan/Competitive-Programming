class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.Counter(nums)        
        
        most = frequency.most_common(k)        
        result = []
        for element, count in most:
            result.append(element)
        
        return result        