class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        n = 0
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                n +=1
            else:
                break
        return strs[0][:n]        
            
            
        
        
            
            
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))