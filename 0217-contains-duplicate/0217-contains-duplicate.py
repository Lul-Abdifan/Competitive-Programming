class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_exe = set()
        for nm in nums:
            if nm in set_exe:
                return True
            else:
                set_exe.add(nm)
        return False        
        