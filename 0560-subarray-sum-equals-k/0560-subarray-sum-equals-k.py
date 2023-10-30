class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        hash_table = {0:1}
        counter = 0
        prefix = 0
        for i in range(len(nums)):
            prefix +=nums[i]
            parted = prefix - k
            if parted in hash_table:
                counter +=hash_table[parted]
            if prefix in hash_table:
                hash_table[prefix] +=1
            else:
                hash_table[prefix] = 1
        return counter        
                
            
         