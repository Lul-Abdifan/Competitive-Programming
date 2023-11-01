class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [0]
        max_height = prefix_sum[0]

        for i in range(len(gain)):
            prefix_elt = prefix_sum[i] + gain[i]
            prefix_sum.append(prefix_elt)
            max_height = max(max_height, prefix_elt)
        return max_height   
            
            
            
        
                       
                           
            
        