class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        def dfs(node, target, visited):

            if node == target:
                return True

            visited.add(node)

            for neigh in graph[node]:
                if neigh not in visited:
                    if dfs(neigh, target, visited):
                        return True

            return False
        
        for u, v in edges:
            visited = set()

            if u in graph and v in graph:
                if dfs(u,v,visited):
                    return [u, v]

            graph[u].append(v)
            graph[v].append(u)
        
        return []