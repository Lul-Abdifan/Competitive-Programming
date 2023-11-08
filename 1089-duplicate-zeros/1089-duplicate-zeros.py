class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i] == 0:
                while i < j:
                    arr[j] = arr[j - 1]
                    j -=1
                arr[i + 1] = 0
                i +=1
                j = len(arr) - 1
                
                
            i += 1
