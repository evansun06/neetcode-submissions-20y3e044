# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def _isBalanced(node: Optional[TreeNode]) -> int:
            nonlocal balanced

            if node is None:
                return -1
            
            left_max_h = _isBalanced(node.left)
            right_max_h = _isBalanced(node.right)

            diff = right_max_h - left_max_h

            if diff > 1 or diff < -1:
                balanced = False
            
            return max(left_max_h, right_max_h) + 1

        _isBalanced(root)

        return balanced