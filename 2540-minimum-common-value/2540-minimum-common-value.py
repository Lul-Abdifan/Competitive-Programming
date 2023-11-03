class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        hashtable = {}
        for i in range(len(nums1)):
            hashtable[nums1[i]] = nums1[i]
        for i in range(len(nums2)):
            if nums2[i] in hashtable:
                return nums2[i]
        return -1   