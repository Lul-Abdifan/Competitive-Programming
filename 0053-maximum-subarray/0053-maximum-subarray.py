class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        gen_max_sum = -math.inf
        
        crt_sum = 0
        
        for i in range(len(nums)):
            crt_sum +=nums[i]
            
            gen_max_sum = max(gen_max_sum,crt_sum)
            
            if crt_sum < 0:
                crt_sum = 0
                
        return gen_max_sum        
        
