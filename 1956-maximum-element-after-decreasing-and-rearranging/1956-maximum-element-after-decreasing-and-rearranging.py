class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        result = 1
        for i in range(1, len(arr)):
            result = min(result+1, arr[i])
        return result
        
        