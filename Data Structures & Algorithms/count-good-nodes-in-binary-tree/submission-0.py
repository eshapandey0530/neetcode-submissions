# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # if not root -> None
        # node.left.val > tree_max -> count += 1
        # node.right.val > tree_max -> count += 1

        def dfs(root, max_value):

            if not root:
                return 0

            count = 0

            if root.val >= max_value:
                max_value = root.val
                count += 1
            
            left = dfs(root.left, max_value)
            right = dfs(root.right, max_value)

            return count + left + right

        return dfs(root, root.val)

        