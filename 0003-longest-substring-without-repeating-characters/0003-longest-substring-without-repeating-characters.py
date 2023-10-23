class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCharacters = 0
        j = 0
        setLists = set()
        for i in range(len(s)):
            if s[i] not in setLists:
                setLists.add(s[i])
                maxCharacters = max(maxCharacters,i - j + 1)
            else:
                while s[i] in setLists :
                         setLists.remove(s[j])
                         j +=1
                         maxCharacters = max(maxCharacters,i - j + 1)
                setLists.add(s[i])
        return maxCharacters