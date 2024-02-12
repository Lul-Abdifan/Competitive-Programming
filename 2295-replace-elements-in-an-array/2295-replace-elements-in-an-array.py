class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dictionary = {}
        
        for i,value in enumerate(nums):
            dictionary[value] = i
    
        for i in range(len(operations)):
            
            x = dictionary[operations[i][0]]
            nums[x] = operations[i][1]
            dictionary[operations[i][1]] = x
        
        return nums    
        