# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Run binary search and maintain left and right bounds init(-inf, inf)
        """

        left = None
        right = None

        curr = root

        while curr != None:
            if target == curr.val:
                return curr.val
            elif target > curr.val:
                left = curr.val
                curr = curr.right
            else:
                right = curr.val
                curr = curr.left
        
        if left is not None and right is not None:
            return left if target - left < right - target else right
        elif left:
            return left
        else:
            return right

        