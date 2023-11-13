class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        store = ""
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1) and j < len(word2):
                store += word1[i]
                store += word2[j]
                i += 1
                j += 1
            elif i < len(word1) and j >= len(word2):
                store += word1[i]
                i += 1
            elif i >= len(word1) and j < len(word2):
                store += word2[j]
                j += 1
        return store
