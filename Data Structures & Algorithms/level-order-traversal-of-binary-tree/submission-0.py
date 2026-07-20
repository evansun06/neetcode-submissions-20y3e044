# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []

        def _dfs(node, depth):

            nonlocal results
            if node is None:
                return
            
            while len(results) - 1 < depth:
                results.append([])
            
            results[depth].append(node.val)

            _dfs(node.left, depth + 1)
            _dfs(node.right, depth + 1)
            
        _dfs(root, 0)

        return results