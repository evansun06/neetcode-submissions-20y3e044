# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def _isValidBST(node: TreeNode, upper: int, lower: int) -> bool:
            # DFS approach

            if node is None:
                return True
            
            if node.val < upper and node.val > lower:
                return _isValidBST(node.left, node.val, lower) and _isValidBST(node.right, upper, node.val)
            else:
                return False

        
        return _isValidBST(root, float('inf'), float('-inf'))
            
