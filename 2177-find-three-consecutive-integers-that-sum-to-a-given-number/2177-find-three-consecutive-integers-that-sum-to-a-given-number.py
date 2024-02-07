class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # Find the mid number
        mid_no = num // 3
        # Get the summation of the consecutive numbers
        nums_summation = mid_no - 1 + mid_no + mid_no + 1 == num
        # return if summation is the same with num
        return [mid_no - 1,mid_no,mid_no + 1] if nums_summation else []
        
        