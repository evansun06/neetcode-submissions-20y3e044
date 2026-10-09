# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def _maxDepth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            else:
                return 1 + max(_maxDepth(node.left), _maxDepth(node.right))
        
        return _maxDepth(root)