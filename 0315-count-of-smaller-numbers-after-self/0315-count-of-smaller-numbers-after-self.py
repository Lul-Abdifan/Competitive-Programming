class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        indices = list(range(len(nums)))

        def merge_sort(start, end):
            if end - start <= 1:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)

            temp = []
            i, j = start, mid
            while i < mid and j < end:
                if nums[indices[i]] <= nums[indices[j]]:
                    temp.append(indices[i])
                    result[indices[i]] += (j - mid)  
                    i += 1
                else:
                    temp.append(indices[j])
                    j += 1
            while i < mid:
                temp.append(indices[i])
                result[indices[i]] += (j - mid)  # Count remaining elements in the right half
                i += 1
            while j < end:
                temp.append(indices[j])
                j += 1

            indices[start:end] = temp

        merge_sort(0, len(nums))
        return result