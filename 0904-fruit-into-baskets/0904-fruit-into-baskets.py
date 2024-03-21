class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        left = 0
        hash_map = defaultdict(int)
        for right in range(len(fruits)):
            hash_map[fruits[right]] +=1
            
            while len(hash_map) > 2:
                hash_map[fruits[left]] -=1
                if hash_map[fruits[left]] == 0:
                    hash_map.pop(fruits[left])
                left +=1
            current_fruits = 0
            for frt in hash_map:
                current_fruits +=hash_map[frt]
                
            max_fruits = max(max_fruits,current_fruits)    
        return max_fruits    
                
                
                
                
            
            
            
    
    
    