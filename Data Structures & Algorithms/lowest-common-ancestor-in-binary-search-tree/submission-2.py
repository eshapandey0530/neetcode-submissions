# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # p <= root and root <= q -> return root
            # return root in all cases and change only if other if conditions satisfy
        # if root.val > p and > q -> lca(root.left)
        # if root.val < p and < q -> lca(root.right)

        if not root:
            return None

        # if root.val >= p.val and root.val <= q.val:

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < p.val  and root.val< q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root