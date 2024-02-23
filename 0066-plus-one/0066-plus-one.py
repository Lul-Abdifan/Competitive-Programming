class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits_tmp ="".join(str(char) for char in digits)
        
        digits_tmp = int(digits_tmp) 
        digits_tmp +=1
      
        return [int(d) for d in str(digits_tmp)]
        
        
        
        
            
        