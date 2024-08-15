class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo: Dict[Tuple[int, int], int] = {}
        
        def coinCounter(i: int, amt: int) -> int:
            if amt == 0:
                return 1
            if amt < 0 or i >= len(coins):
                return 0
            
            if (i, amt) in memo:
                return memo[(i, amt)]
            
            minimized = coinCounter(i, amt - coins[i]) + coinCounter(i + 1, amt)
            memo[(i, amt)] = minimized
            return minimized
        
        return coinCounter(0, amount)