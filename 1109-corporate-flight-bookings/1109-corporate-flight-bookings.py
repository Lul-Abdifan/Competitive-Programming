class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0]*(n + 2)
        output = []
        
        for q in bookings:
            l,r,amount = q
            prefix[l] += amount
            prefix[r + 1]-=amount
        
        for i in range(1,len(prefix)):
            prefix[i] = prefix[i - 1] + prefix[i]
            
        for i in range(1,len(prefix) - 1):
            output.append(prefix[i])
            
        return output    
           