class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neigh in graph[node]:
                dfs(neigh)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count
