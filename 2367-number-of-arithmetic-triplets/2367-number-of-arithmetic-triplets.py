class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i + 1,len(nums)):
                y = nums[j]
                if y - x == diff:
                    for k in range(j + 1,len(nums)):
                        z = nums[k]
                        if z - y == diff:
                            counter +=1
        return counter                   
                            
                             
                
                
                
                
                
        
        