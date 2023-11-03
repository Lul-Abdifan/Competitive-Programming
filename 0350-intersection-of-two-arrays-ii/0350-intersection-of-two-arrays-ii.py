class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashtable = {}
        store = []
        for num in nums1:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1
        for num in nums2:
            if num in hashtable and hashtable[num] >0:
                hashtable[num] -= 1
                store.append(num)
        return store     