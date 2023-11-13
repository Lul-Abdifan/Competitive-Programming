class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original_number = x
        reversed_number = 0
        while x > 0:
            reversed_number = reversed_number * 10 + x%10
            x //=10
        return reversed_number == original_number    

