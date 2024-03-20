from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        window_counter = defaultdict(int)
        
        for num in s[:len(p)]:
            window_counter[num] += 1
        
        anagram_window = Counter(p)
      
        right = len(p) - 1
        left = 0
        
        while right < len(s):
            if window_counter == anagram_window:
                res.append(left)
            right +=1    
            
            if right < len(s):
                window_counter[s[right]] += 1
                window_counter[s[left]] -= 1
                
                if window_counter[s[left]] == 0:
                    del window_counter[s[left]]
            
            
            left += 1
            
        return res