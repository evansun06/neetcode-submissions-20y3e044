# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        InOrder traversal tells us:
        The nodes relative positions left and right of each other

        PreOrder traversal tells us:
        preorder[0] is the root node

        preorder [1,2,3,4]
        inorder  [2,1,3,4]

        """

        pre_order_idx = 0
        inorder_idx_map = {
            num: i for i, num in enumerate(inorder)
        }

        def preOrderBuild(left, right):
            nonlocal pre_order_idx

            if right < left:
                return None
            
            root_value = preorder[pre_order_idx]
            pre_order_idx += 1

            root = TreeNode(root_value)
            mid = inorder_idx_map[root_value]

            root.left = preOrderBuild(left, mid - 1)
            root.right = preOrderBuild(mid + 1, right)

            return root

        return preOrderBuild(0, len(preorder) - 1)
