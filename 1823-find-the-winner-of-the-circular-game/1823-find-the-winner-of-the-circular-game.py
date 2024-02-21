class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Create a list of numbers from 1 to n
        people = list(range(1, n + 1))
        
        # Initialize the index of the current person to be removed
        idx = 0
        
        # Iterate until there is only one person left
        while len(people) > 1:
            # Calculate the index of the person to be removed
            idx = (idx + k - 1) % len(people)
            # Remove the person at the calculated index
            people.pop(idx)
        
        # Return the remaining person who is the winner
        return people[0]