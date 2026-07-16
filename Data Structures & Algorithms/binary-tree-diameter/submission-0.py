# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0

        def get_d(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            h_left = get_d(node.left)
            h_right = get_d(node.right)
            d = h_left + h_right 

            if d > self.max_d:
                self.max_d = d
            
            return max(h_left, h_right) + 1
        
        get_d(root)
        return self.max_d
        
