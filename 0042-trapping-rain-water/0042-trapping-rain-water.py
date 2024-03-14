class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        max_val = 0
        res = 0
        for i in range(len(height)):
            maxLeft[i] = max_val
            if height[i] > max_val:
                max_val = height[i]
        max_val = 0        
        for j in range(len(height) - 1,-1,-1):
            maxRight[j] = max_val
            if height[j] > max_val:
                max_val = height[j]        
       
        for i in range(len(height)):
            if min(maxLeft[i],maxRight[i]) - height[i] > 0:
                res += min(maxLeft[i],maxRight[i]) - height[i]
        return res        
            

        