class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
      
        nums.sort()  
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i - 1]
                      
        def binary_search(target):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left  

        result = []

        for query in queries:
            index = binary_search(query)  
            result.append(index)  

        return result


        