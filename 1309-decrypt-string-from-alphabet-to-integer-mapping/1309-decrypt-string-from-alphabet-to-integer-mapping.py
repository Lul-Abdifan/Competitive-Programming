class Solution:
    def freqAlphabets(self, s: str) -> str:

        characters = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                characters +=  chr(ord('a') + (int(s[i:i + 2]) - 1))
                i = i + 3
            else:
                characters +=  chr(ord('a') + (int(s[i]) - 1))
                i = i + 1
        return characters