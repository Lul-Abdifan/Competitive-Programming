class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        length = min(len(list(word1)),len(list(word2)))
        
        for i in range(length):
            string +=word1[i] + word2[i]
            
        string +=word1[i + 1:] + word2[i + 1:]
        return string
