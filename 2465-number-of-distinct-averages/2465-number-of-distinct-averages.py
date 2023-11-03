class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        my_dict = {}
        nums.sort()
        i,j = 0 ,len(nums) - 1
        while(i < j):
            avr = (nums[i] + nums[j])/2
            if avr in my_dict:
                my_dict[avr] +=1
            else:
                my_dict[avr] = 1
            i +=1
            j -=1
        return len(my_dict)       
            