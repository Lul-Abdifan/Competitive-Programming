class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        count_chr = 0
        count_t = 0
        count_f = 0
        max_length = 0
        left = 0


        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                count_t +=1
            else:
                count_f +=1
            while min(count_f,count_t) > k:
                if answerKey[left] == 'T':
                    count_t -=1
                else:
                    count_f -=1
                left +=1
            max_length = max(max_length,right - left + 1)  
        return max_length    
                
                    
                    
                
            
            
        
        
         
        
        



    
    