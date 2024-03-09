class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        left = 0
        right = len(people) - 1
        counter = 0
        while left <= right:
            if people[right] + people[left] <= limit:
                counter +=1
                right -=1
                left +=1
                
            else:
                counter +=1
                right -=1
        return counter       
            
            
                
                    
        