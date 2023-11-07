class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i <= j:
            tmp = s[j]
            s[j] = s[i]
            s[i] = tmp
            j -=1
            i +=1
        """
        Do not return anything, modify s in-place instead.
        """
        