class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count = 0
        
        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if i + 1 < len(strs) and strs[i + 1][j] < strs[i][j]:
                    count +=1
                    break
        return count
