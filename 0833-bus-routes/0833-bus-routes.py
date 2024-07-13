class Solution:
    def numBusesToDestination(self, ro: List[List[int]], sr: int, tar: int) -> int:
        d=defaultdict(list)
        for i,val in enumerate(ro):
            for s in val:
                d[s].append(i)
        if sr==tar:
            return 0
        elif sr not in d:
            return -1
        vis=set()
        bus=set()
        ans=0
        queue=deque()
        queue.append(sr)
        vis.add(sr)
        while queue:
            l=len(queue)

            for i in range(l):
                ele=queue.popleft()
                if ele==tar:
                    return ans
                bval=d[ele]
                for b in bval:
                    if b not in bus:
                        for each in ro[b]:
                            if each not in vis:
                                queue.append(each)
                                vis.add(each)
                        bus.add(b)
            ans+=1 
        return -1

        