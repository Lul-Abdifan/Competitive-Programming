class Solution:
     def reverseWords(self, s: str) -> str:
         s = s.strip() 
         left,right = len(s) - 1,len(s) - 1
         
         result = []
            
        
         while left >= 0:
             while left >= 0 and s[left] != " ":
                left -=1
             result.append(s[left + 1:right + 1]) 
         
             while left >=0 and s[left] == " ":
                left -=1
             right = left  
             
         return ' '.join(result)
             
        
        