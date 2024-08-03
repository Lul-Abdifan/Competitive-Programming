from typing import List
from collections import defaultdict, deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        revGraph = defaultdict(list)
        indegree = [0] * len(graph)
        
        for i, nodes in enumerate(graph):
            for node in nodes:
                revGraph[node].append(i)
            indegree[i] = len(nodes)

        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        results = []

        while queue:
            node = queue.popleft()
            results.append(node)
            for predecessor in revGraph[node]:
                indegree[predecessor] -= 1
                if indegree[predecessor] == 0:
                    queue.append(predecessor)

        return sorted(results)
