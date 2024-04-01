class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints) - k
        pref_sum = sum(cardPoints[:length])
        tmp_sum = sum(cardPoints) - pref_sum
        max_sum = tmp_sum
        left = 0
        
        while length < len(cardPoints):
            tmp_sum = tmp_sum + cardPoints[left] - cardPoints[length]
            max_sum = max(max_sum,tmp_sum)
            length +=1
            left +=1
            
        return max_sum
        
        

        
       
        
        
        