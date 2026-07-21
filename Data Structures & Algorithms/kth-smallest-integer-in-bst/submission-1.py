# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        k_smallest = root.val

        def _dfs(node: Optional[TreeNode]):
            nonlocal count, k_smallest

            if node is None or count == k:
                return
            
            _dfs(node.left)

            count += 1

            if count == k:
                k_smallest = node.val
            
            _dfs(node.right)
                
        _dfs(root)

        return k_smallest
