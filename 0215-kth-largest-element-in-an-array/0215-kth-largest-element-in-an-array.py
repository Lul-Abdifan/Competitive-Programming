class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_array = []

        for num in nums:
            heappush(heap_array,num)  
            if len(heap_array) > k:
                heappop(heap_array)
              
        return heappop(heap_array)        
        