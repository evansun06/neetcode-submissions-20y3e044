# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
                    4
                3       6
            1
            1   3   4   6
        """

        count = 0
        result = None


        def inOrderTraversal(node: Optional[TreeNode]):
            nonlocal count
            nonlocal k
            nonlocal result

            if node is None:
                return
            
            inOrderTraversal(node.left)
            count += 1
            if count == k:
                result = node.val
                return
            inOrderTraversal(node.right)

        inOrderTraversal(root)
        
        return result
            


        