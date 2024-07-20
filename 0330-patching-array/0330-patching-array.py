class Solution:
    def minPatches(self, nums: List[int], target: int) -> int:
        patch_count, current_index, coverage_limit = 0, 0, 1

        while coverage_limit <= target:
            if current_index < len(nums) and nums[current_index] <= coverage_limit:
                coverage_limit += nums[current_index]
                current_index += 1
            else:
                coverage_limit *= 2
                patch_count += 1

        return patch_count