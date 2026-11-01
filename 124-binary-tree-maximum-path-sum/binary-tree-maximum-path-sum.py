# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans = -inf
        def dfs(node):
            nonlocal ans
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            s = left + right + node.val
            ans = max(ans, s)
            return max(max(left, right) + node.val, 0)
        dfs(root)
        return ans