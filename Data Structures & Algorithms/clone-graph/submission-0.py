"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        visited = set()
        hmap = {}
        start = node
        
        def dfs(node):
            
            if node in visited:
                return
            
            visited.add(node)
            hmap[node] = Node(node.val)

            for neigh in node.neighbors:
                dfs(neigh)

        dfs(start)

        for old_node, new_node in hmap.items():
            for neigh in old_node.neighbors:
                new_node.neighbors.append(hmap[neigh])


        return hmap[start]





