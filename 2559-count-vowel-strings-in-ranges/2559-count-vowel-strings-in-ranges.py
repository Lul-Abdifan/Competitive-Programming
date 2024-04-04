class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]*(len(words) + 1)
        vowels = "aeiou"
        output = []
        for i in range(1,len(prefix)):
            if words[i - 1][0] in vowels and words[i - 1][-1] in vowels:
                prefix[i] = 1
        print(prefix)       
        for i in range(1,len(prefix)):
            prefix[i] = prefix[i - 1] + prefix[i]
        print(prefix)       
    
        for query in queries:
            l,r= query
            output.append(prefix[r + 1] - prefix[l])
            
        return output    
            
            
        
        # 0 1 0 1 1 1
        # 0 1 1 2 3 4
