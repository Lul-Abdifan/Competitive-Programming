class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            queue = deque([(start, 1.0)])
            visited = set()

            while queue:
                current, product = queue.popleft()
                if current == end:
                    return product
                visited.add(current)
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        queue.append((neighbor, product * value))
            return -1.0

        results = []
        for C, D in queries:
            result = bfs(C, D)
            results.append(result)
        
        return results      