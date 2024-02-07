class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # countering the 
        # update the maximum to counter if it is greater than the previous 
        maximum = 0
        counter = 0
        for n in nums:
            if n == 1:
                counter +=1
                maximum = max(maximum,counter)
            else:
                counter = 0
        return maximum        
                
            
        
        
        
        
        