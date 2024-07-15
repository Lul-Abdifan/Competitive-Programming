class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        piles = [-i for i  in piles]
        heapify(piles)
        for i in range(k):
            popped =heappop(piles)
            total += math.ceil(popped/2)
            heappush(piles,popped//2)
        return total