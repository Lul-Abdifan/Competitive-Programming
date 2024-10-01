class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:


        graph = collections.defaultdict(list) 

        for u, v, d in roads: 
            graph[u].append((v, d))
            graph[v].append((u, d))

        answer = float("inf") 

        queue = collections.deque()
        queue.append((1))

        visited = set()

        while queue:
            node = queue.popleft()

            if node in visited:
                continue
        
            for neighbour, distance in graph[node]:
                if neighbour not in visited:
                    answer = min(answer, distance)
                    queue.append((neighbour))

            visited.add(node)

        return answer