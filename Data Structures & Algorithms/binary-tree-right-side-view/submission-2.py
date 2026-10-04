# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        bfs O(n) + O(n) space:
            - left to right per layer of the binary tree
        """
        if root is None:
            return []
            
        q = deque()
        q.append(root)
        result = []

        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

                if i == n - 1:
                    result.append(node.val)
        
        return result

        