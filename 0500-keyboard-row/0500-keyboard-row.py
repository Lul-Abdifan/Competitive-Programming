class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set_1 = set("qwertyuiop")
        set_2 = set("asdfghjkl")
        set_3 = set("zxcvbnm")
        
        result = []
        
        for word in words:
            if set(word.lower()).issubset(set_1) or set(word.lower()).issubset(set_2) or set(word.lower()).issubset(set_3):
                result.append(word)
        
        return result        
            
        
        
 
             
        
        