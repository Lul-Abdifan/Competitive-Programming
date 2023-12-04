class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False

        l, r = 0, len(arr) - 1

        while l < len(arr) - 1 and arr[l] < arr[l + 1]:
            l += 1
        while r > 0 and arr[r - 1] > arr[r]:
            r -=1
           


        return 0 < l == r < len(arr) - 1