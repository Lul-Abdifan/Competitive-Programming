from collections import deque, defaultdict

class Solution:
    def check_cycle(self, graph, numCourses):
        indegree = [0] * numCourses
        for i in range(numCourses):
            for j in graph[i]:
                indegree[j] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        while queue:
            u = queue.popleft()
            visited += 1
            for t in graph[u]:
                indegree[t] -= 1
                if indegree[t] == 0:
                    queue.append(t)
        
        return visited != numCourses
    
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
        
        if not prerequisites:
            return True
        
        if self.check_cycle(graph, numCourses):
            return False
        
        return True
