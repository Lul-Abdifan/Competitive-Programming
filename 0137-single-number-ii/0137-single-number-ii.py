class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        double = 0
        for num in nums:
            single = (single ^ num) & ~double
            double = (double ^ num) & ~single

        return single