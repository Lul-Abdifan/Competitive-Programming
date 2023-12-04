class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_value = -1
        for i in range(len(arr) - 1,-1,-1):
            current = arr[i]
            arr[i] = max_value
            max_value = max(current,max_value)
            
                
            
            
            
        return arr    
        