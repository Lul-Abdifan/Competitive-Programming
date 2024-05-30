class Solution:
    def numberOfSteps(self, num: int) -> int:
        def recursion(n,counter):
            if n == 0:
                return counter

            if n%2 == 0:
                return recursion(n//2,counter + 1)
            else:
                return recursion(n - 1,counter + 1)
        return recursion(num,0)        

        