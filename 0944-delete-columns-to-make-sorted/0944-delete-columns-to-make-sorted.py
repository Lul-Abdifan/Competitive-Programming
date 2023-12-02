class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        del_counter = 0
        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j + 1][i] < strs[j][i]:
                    del_counter +=1
                    break
        return del_counter            
            
        