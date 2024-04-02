class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passes = [0]*(1001)
        
        for i in range(len(trips)):
            no_p,start,end = trips[i]
            if no_p > capacity:
                return False
                
            passes[start] += no_p
            passes[end] -= no_p
            
        for i in range(1,1001):
            passes[i] = passes[i] + passes[i - 1]
            if passes[i] > capacity:
                return False
        return True    
        

        
        
        
        
      