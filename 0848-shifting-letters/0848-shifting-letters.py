class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix = [0]*(len(s) + 1)
        offset = ord('a')

        string = list(s)
        for i in range((len(prefix) - 2), -1,-1):
            prefix[i] = (prefix[i + 1] + shifts[i])%26

        
        for i in range(len(s)):
            no = (ord(s[i]) + prefix[i])
            string[i] = chr(no) if no < offset + 26 else chr(no - 26)
            
        
        
        return "".join(string)