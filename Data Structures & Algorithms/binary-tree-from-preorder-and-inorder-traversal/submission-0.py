# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #             [2]
        #         [1]     [4]
        #       [5] [3]   
        #            [9]

        # pre: [2, 1, 5, 3, 9, 4]
        # in:  [5, 1, 3, 9, 2, 4]

        pre_order_index = 0
        in_order_index = {
            value:index
            for index, value in enumerate(inorder)
        }

        def build(left, right) -> Optional[TreeNode]:
            nonlocal pre_order_index, in_order_index

            if left > right:
                return None

            root_val = preorder[pre_order_index]
            pre_order_index += 1

            root = TreeNode(root_val)
            mid = in_order_index[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(preorder) - 1)








