class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p = 0
        t = 0
        counter = 0
        
        while p < len(players) and t < len(trainers):
            tmp = players[p]
            
            while t < len(trainers) and trainers[t] < tmp:
                t +=1
            if t < len(trainers) and tmp <= trainers[t]:
                counter +=1
                t +=1
            p +=1    
        return counter       
                
            
            
            
            
        # players = [4,7,9],
        # trainers =[2,5,8,8]
        
        