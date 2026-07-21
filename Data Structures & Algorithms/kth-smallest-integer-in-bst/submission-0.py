# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []

        def in_order_traversal(node: TreeNode):
            nonlocal in_order

            if node is None:
                return
            
            in_order_traversal(node.left)
            in_order.append(node.val)
            in_order_traversal(node.right)

        in_order_traversal(root)

        return in_order[k-1]