class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegrees = [0]*numCourses
        graph = defaultdict(list)

        for nm in prerequisites:
            a,b = nm
            graph[b].append(a)
            inDegrees[a] +=1

        queue = deque([nm for nm in range(numCourses) if inDegrees[nm] == 0])  
        print(queue)  
        res = []
        if not queue:
            return res
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for vrx in graph[cur]:
                inDegrees[vrx] -= 1
                if inDegrees[vrx] == 0:
                    queue.append(vrx)
        return res if len(res) == numCourses else []

        