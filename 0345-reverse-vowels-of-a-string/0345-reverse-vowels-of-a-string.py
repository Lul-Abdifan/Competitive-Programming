class Solution:
    def reverseVowels(self, s: str) -> str:
        array = list(s)
        i = 0
        j = len(array) - 1
        vowels = 'aeiouAEIOU'  # Include both lowercase and uppercase vowels

        while i < j:
            while i < j and array[i] not in vowels:
                i += 1
            while i < j and array[j] not in vowels:
                j -= 1

            if i < j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        return "".join(array)
