class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool: 
        
        # joining each individual lists of the array
        # compare if the same
        if ''.join(word1) == ''.join(word2):
            return True
        else:
            return False
        
        