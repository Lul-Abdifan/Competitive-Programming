class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        max_you_take = 0
        
        no_piles = len(piles)//3

        
        i = no_piles
        while i < len(piles):
            
            max_you_take +=piles[i]
            i +=2
            
        return max_you_take    
            
            
            
        
        
        
        
        
        
        

        
      
         
        
        
