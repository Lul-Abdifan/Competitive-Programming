class Solution:
    def isHappy(self, n):
        seen = set()  # Create an empty set to store numbers we've seen

        while n not in seen:  # Continue until we encounter a number we've seen before
            seen.add(n)  # Add the current number to the set of seen numbers
            n = sum([int(x) ** 2 for x in str(n)])  # Replace 'n' with the sum of the squares of its digits

        return n == 1  # Return True if we ended up with 1 (a happy number), otherwise return False

        