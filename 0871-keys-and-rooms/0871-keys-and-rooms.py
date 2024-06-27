class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visited = set()
        visited.add(0)
        queue = deque([0])

        for i in range(len(rooms)):
            adjList[i].extend(rooms[i])
        
        
        while queue:
                node = queue.popleft()

                for nm in adjList[node]:
                  if nm not in visited:
                    visited.add(nm)
                    queue.append(nm)
        print(rooms,visited)            
        return len(rooms) == len(visited)        
                




        
            

        
                      





        

        return False  
        