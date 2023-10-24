class Solution:
    def maxPower(self, s: str) -> int:
        j = 0
        max_string = 1
        for i in range(1,len(s)):
            if s[i] == s[j]:
                max_string = max(max_string,i - j + 1)
            else:
                j = i
                
                
        return max_string    
    
    
        