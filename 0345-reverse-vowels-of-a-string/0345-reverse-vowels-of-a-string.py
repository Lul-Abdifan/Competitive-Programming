class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        given_string = list(s)
        i = 0
        j = len(given_string) - 1
        while i < j:
            while i < j and given_string[i] not in vowels:
                i +=1
            while i < j and given_string[j] not in vowels:
                j -=1
            if given_string[i] != given_string[j]:
                tmp = given_string[i]
                given_string[i] = given_string[j]
                given_string[j] = tmp
            i +=1
            j -=1
        return "".join(given_string)    
                
            
            
            
            
            
        