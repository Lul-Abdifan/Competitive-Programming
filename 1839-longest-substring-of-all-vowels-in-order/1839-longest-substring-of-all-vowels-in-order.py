class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if len(word) < 5:
            return 0
        

        no_beautiful = 0
        vowel_set = set()
        left = 0
        for right in range(len(word)):
            
            if right < len(word) - 1 and word[right] <= word[right + 1]:
                vowel_set.add(word[right])
                

                if len(vowel_set) == 5:
                    no_beautiful = max(no_beautiful,right - left + 1)
                    
            else:
                vowel_set.add(word[right])
                if len(vowel_set) == 5:
                    no_beautiful = max(no_beautiful,right - left + 1)
                vowel_set.clear()
               
                
                left = right + 1
                
        return no_beautiful    
                    
                
            
            
        