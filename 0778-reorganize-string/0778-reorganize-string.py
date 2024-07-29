class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        res = ""
        char_cnt = [(-cn, c) for c, cn in counter.items()]
        heapq.heapify(char_cnt)
       
        while len(char_cnt) > 1:
            cn1, ch1 = heapq.heappop(char_cnt)
            cn2, ch2 = heapq.heappop(char_cnt)

            res += ch1
            res += ch2

            cn1 += 1
            cn2 += 1

            if cn1 < 0:
                heapq.heappush(char_cnt, (cn1, ch1))
            if cn2 < 0:
                heapq.heappush(char_cnt, (cn2, ch2))
                
        if char_cnt:
            cn, ch = char_cnt.pop()
            if cn < -1:
                return ""
            res += ch 
                 
        return res