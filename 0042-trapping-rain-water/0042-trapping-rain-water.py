class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        maxLeft = 0
        maxRight = 0
        rain = 0
        
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    rain += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    rain += maxRight - height[right]
                right -= 1
                
        return rain