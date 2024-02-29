class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        tmp  = sorted(nums)
        res = [] 
        mapping = {}
        
        for i,value in enumerate(tmp):
            if value not in mapping:
                mapping[value] = i
                
        
         
        for num in nums:
            res.append(mapping[num])
            
        return res    
            
        
        