# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        ans = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal ans
            left = node.left
            if left and not left.left and not left.right:
                ans += left.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans