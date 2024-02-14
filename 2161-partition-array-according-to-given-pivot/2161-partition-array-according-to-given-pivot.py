class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lists = []
        pivot_counts = 0
        
        i = 0
        j = 0
        
        while j < len(nums):
            if nums[j] == pivot:
                pivot_counts +=1
            if nums[j] < pivot:
                lists.append(nums[j])
            j +=1
        
        k = 0
        
        while k < pivot_counts:
            lists.append(pivot)
            k +=1
                
                
        while i < len(nums):  
            if nums[i] > pivot:
                lists.append(nums[i])
            i +=1
           
                
        return lists
        