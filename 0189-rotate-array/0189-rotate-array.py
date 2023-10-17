class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        last_k = nums[-k:] 
        for i in range(len(nums)-1,k-1,-1):
            nums[i]=nums[i-k]
        for i in range(k):
            nums[i] =  last_k[i]    
  