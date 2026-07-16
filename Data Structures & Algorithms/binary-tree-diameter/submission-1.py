# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0

        def get_d(node: Optional[TreeNode]) -> int:
            nonlocal max_d
            if node is None:
                return 0

            h_left = get_d(node.left)
            h_right = get_d(node.right)
            d = h_left + h_right 

            if d > max_d:
                max_d = d
            
            return max(h_left, h_right) + 1
        
        get_d(root)
        return max_d
        
