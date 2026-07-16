class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # if len(edges) != n-1:
        #     return False

        # graph = defaultdict(list)

        # for a,b in edges:
        #     graph[a].append(b)
        #     graph[b].append(a)
        
        # visited = set()

        # def dfs(node, par):

        #     if node in visited:
        #         return True

        #     if node == par:
        #         return False

        #     visited.add(node)

        #     for neigh in graph[node]:
        #         if not dfs(neigh, node):
        #             return False

        #     return True
        
        
        # for i in range(n):
        #     if not dfs(i, -1):
        #         return False

        # return len(visited) == n
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if len(edges) != n - 1:
            return False
        
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

        dfs(0)

        return len(visited) == n