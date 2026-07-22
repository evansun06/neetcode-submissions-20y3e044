# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpathsum = [root.val]
        
        def _dfs(node: Optional[TreeNode]) -> int:

            if node is None:
                return 0

            left_max = _dfs(node.left)
            right_max = _dfs(node.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            maxpathsum[0] = max(maxpathsum[0], node.val + left_max + right_max)
            
            return max(node.val + left_max, node.val + right_max)

        _dfs(root)

        return maxpathsum[0]

        