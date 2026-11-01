# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        x = root.val
        if x < p.val and x < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif x > q.val and x > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root