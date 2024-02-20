class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        difference_to_arrive = abs(target[0]) + abs(target[1])
        
        for ghost in ghosts:
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= difference_to_arrive:
                return False
        return True    
                
        
        
        