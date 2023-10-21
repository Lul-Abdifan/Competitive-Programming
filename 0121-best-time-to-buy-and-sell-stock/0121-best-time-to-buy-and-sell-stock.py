class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         minimum = prices[0]
         maximum = prices[0]
         maxProfit = int(maximum - minimum)
         if len(prices) == 0:
             return 0

         for i in range(len(prices)):
              if prices[i] <= minimum:
                    minimum = prices[i]
                    maximum = prices[i]
              else:
                maximum = max(maximum,prices[i])
                maxProfit =max(maxProfit,maximum - minimum)      
         return maxProfit

        

