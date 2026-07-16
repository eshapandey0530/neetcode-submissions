# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        seq = []

        # in - order

        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            seq.append(root.val)
            dfs(root.right)

            return root

        dfs(root)

        return seq[k-1]
