class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        minimized_capacity = capacity
        
        for i in range(len(plants)):
            if minimized_capacity >= plants[i]:
                minimized_capacity -=plants[i]
                steps +=1
            else:
                    minimized_capacity = capacity
                    steps +=i
                    minimized_capacity -=plants[i]
                    steps += i + 1
        return steps           

        