class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memoization = {}

        def dp(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0           

            if (i, j) in memoization:
                return memoization[(i, j)]

            if s[i] != t[j]:
                memoization[(i, j)] = dp(i + 1, j) 
            else:
                memoization[(i, j)] = dp(i + 1, j + 1) + dp(i + 1, j) 

            return memoization[(i, j)]

        return dp(0, 0)
        