class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sets(fun_res,nums):

            if not nums:
                
                
                return [fun_res]

            val = nums[0]

            # left = sets(fun_res,nums[1:])
            # right = sets(fun_res + [val],nums[1:])
            return sets(fun_res,nums[1:]) + sets(fun_res + [val],nums[1:])
          
        
        return sets([],nums) 
        



        