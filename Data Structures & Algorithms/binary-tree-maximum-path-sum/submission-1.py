# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpathsum = -1001
        
        def _dfs(node: Optional[TreeNode]) -> int:
            nonlocal maxpathsum

            if node is None:
                return 0

            left_max = _dfs(node.left)
            right_max = _dfs(node.right)

            s = max(node.val + left_max + right_max, node.val, node.val + left_max, node.val + right_max)

            if s > maxpathsum:
                maxpathsum = s
            
            return max(node.val + left_max, node.val + right_max, node.val)

        _dfs(root)

        return maxpathsum

        