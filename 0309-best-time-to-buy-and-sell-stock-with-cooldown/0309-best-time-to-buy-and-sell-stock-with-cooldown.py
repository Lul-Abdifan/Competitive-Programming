class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0
        sell, buy, previous_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(previous_sell - price, prev_buy)
            previous_sell = sell
            sell = max(prev_buy + price, previous_sell)
        return sell
            