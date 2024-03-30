class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        initial_state = {0:1}
        prefix = 0
        cnt = 0
        for right in range(len(nums)):
            prefix +=nums[right]
            
            prefix_prev = prefix%k
            
            if prefix_prev in initial_state:
                cnt +=initial_state[prefix_prev]
                initial_state[prefix_prev] +=1
            else:
                initial_state[prefix_prev] = 1
        return cnt        
                
                
            
        

    
