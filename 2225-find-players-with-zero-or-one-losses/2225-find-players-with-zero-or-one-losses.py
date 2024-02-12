class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dictionary = {}
        
        for i in range(len(matches)):
            if matches[i][1] not in dictionary:
                dictionary[matches[i][1]] = 1    
            
            
            else:
                dictionary[matches[i][1]] += 1
                
        winners = [matches[i][0] for i in range(len(matches)) if matches[i][0] not in dictionary] 
        
        lost_1match = [num for num in dictionary if dictionary[num] == 1]
        
        return [sorted(list(set(winners))),sorted(lost_1match)]
        

                
                
        