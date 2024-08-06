class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n <= 3:
                return n
            if n not in memo:
                memo[n] = helper(n - 2) + helper(n - 1)
            return memo[n]   
        return helper(n)       
        