class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])
        heap = []
        total_quality = 0
        min_cost = float('inf')
        
        for ratio, worker_quality in workers:
            heapq.heappush(heap, -worker_quality)
            total_quality += worker_quality
            if len(heap) > k:
                total_quality += heapq.heappop(heap)
            if len(heap) == k:
                min_cost = min(min_cost, total_quality * ratio)
        
        return min_cost
