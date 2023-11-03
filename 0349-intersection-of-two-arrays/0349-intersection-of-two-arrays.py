class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashtable = set(nums1)
        intersection_element = set()
        
          
        for num in nums2:
            if num in hashtable:
               intersection_element.add(num)
        return list(intersection_element)
        