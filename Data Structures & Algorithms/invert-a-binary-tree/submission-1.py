# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def _invertTree(node: Optional[TreeNode]) -> Optional[TreeNode]:

            if node is None:
                return None
            else:
                temp = node.left
                node.left = _invertTree(node.right)
                node.right = _invertTree(temp)
                return node

        return _invertTree(root)