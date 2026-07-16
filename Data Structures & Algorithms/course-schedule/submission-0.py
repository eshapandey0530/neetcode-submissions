class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[a].append(b)

        visited = set()
        visiting = set()

        def dfs(node):
            
            if node in visited:
                return True

            if node in visiting:
                return False

            visiting.add(node)

            for neigh in graph[node]:
                if not dfs(neigh):
                    return False

            visiting.remove(node)
            visited.add(node)

            return True

        for num in range(numCourses):
            if not dfs(num):
                return False

        return True