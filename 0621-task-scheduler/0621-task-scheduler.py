class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        characters = [0]*26
        for i in range(len(tasks)):
            characters[ord(tasks[i]) - ord('A')] +=1

        characters.sort()

        slots = (characters[25] - 1) * n
        for i in range(24,-1,-1):
            slots -= min(characters[25] - 1,characters[i])
        if slots <= 0:
            return len(tasks)
        return len(tasks) + slots
            