class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hashtable = {}
        counter = 0
        
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                counter += hashtable[num]
                hashtable[num] += 1

        return counter
