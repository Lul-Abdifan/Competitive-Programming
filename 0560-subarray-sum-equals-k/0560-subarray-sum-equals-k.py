class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        initial_state = {0:1}
        prefix = 0
        cnt = 0
        for right in range(len(nums)):
            prefix += nums[right]
            
            tmp_pref = prefix - k
            if tmp_pref in initial_state:
                cnt +=initial_state[tmp_pref] 
            
            
            if prefix not in initial_state:
                initial_state[prefix] = 1
           
            else: 
                initial_state[prefix] += 1
               
        return cnt        
                
                
      
        
        
        

        

        