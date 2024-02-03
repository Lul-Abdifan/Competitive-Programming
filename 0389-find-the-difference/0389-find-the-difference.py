class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)
        
        difference = counter_t - counter_s

        return list(difference.keys())[0]
        

            