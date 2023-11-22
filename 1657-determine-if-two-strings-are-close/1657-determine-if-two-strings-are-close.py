class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        
        dict_1 = Counter(word1)
        dict_2 = Counter(word2)
        
        for num in dict_1.values():
            if num not in dict_2.values():
                return False
        for num in dict_2.values():
            if num not in dict_1.values():
                return False        
   
        for num in dict_1.keys():
            if num not in dict_2.keys():
                return False
        counter_1 = Counter(dict_1.values())
        counter_2 = Counter(dict_2.values())
        
        for key,value in counter_1.items():
            if value != counter_2[key]:
                return 0
            
                
     
        return 1