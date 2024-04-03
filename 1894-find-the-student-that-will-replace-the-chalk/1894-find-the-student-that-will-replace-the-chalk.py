class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tmp_sum = k%sum(chalk)
        
        to_get_sum = 0
        
        for i in range(len(chalk)):
            to_get_sum +=chalk[i]
            
            if to_get_sum >tmp_sum:
                return i
        
        
        
25
    
  
        