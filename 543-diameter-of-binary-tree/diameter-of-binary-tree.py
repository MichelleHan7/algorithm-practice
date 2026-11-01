# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            if node is None:
                return -1
            nonlocal ans
            left = dfs(node.left)
            right = dfs(node.right)
            ans = max(ans, left + right + 2)
            return 1 + max(left, right)
        dfs(root)
        return ans