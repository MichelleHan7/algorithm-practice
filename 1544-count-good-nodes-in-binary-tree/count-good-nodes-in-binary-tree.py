# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, m):
            nonlocal ans
            if node is None:
                return 0
            if node.val >= m:
                ans += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, m)
                dfs(node.right, m)
        dfs(root, -inf)
        return ans