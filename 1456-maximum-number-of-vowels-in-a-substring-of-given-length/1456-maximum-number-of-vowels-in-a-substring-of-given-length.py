class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        counter  = 0
        max_vowels = float('-inf')
        i = 0
        j = 0
        
        while i < len(s):
            if i < k:
                if s[i] in vowels:
                    counter +=1
                    max_vowels = max(max_vowels,counter)
                i +=1
                continue
            elif i >= k:
                if s[i] not in vowels and s[j] in vowels:
                    counter -=1
                if s[i] in vowels and s[j] not in vowels:
                    counter +=1
                max_vowels = max(max_vowels,counter)
            i +=1
            j +=1

        return max_vowels            
                
                
                
                    
                    
                    
                
                
                
        