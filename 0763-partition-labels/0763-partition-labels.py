class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        look_up = set()
        result = []
        l, r = 0, 0
        
     
        
        
        while r < len(s):
            counter[s[r]] -= 1
            look_up.add(s[r])
            if counter[s[r]] == 0:
                del counter[s[r]]
                if s[r] in look_up:
                     look_up.remove(s[r])
                     if not look_up:
                        result.append(r - l + 1)
                        l = r + 1
                
  
            r += 1
    
        
        return result