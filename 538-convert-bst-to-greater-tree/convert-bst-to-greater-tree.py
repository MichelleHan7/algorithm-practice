# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        t = 0
        def dfs(node, total):
            nonlocal t
            if not node:
                return 
            dfs(node.right, t)
            t += node.val
            node.val = t
            dfs(node.left, t)
        dfs(root, 0)
        return root