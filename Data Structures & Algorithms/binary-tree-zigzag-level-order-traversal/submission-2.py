# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        q = deque()
        depth = 0
        result = []

        q.append(root)

        while q:
            
            size = len(q)
            level = [0] * size
            
            for i in range(size):
                node = q.popleft()

                if depth % 2 == 1:
                    idx = size - 1 - i
                else:
                    idx = i

                level[idx] = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(level)
    
            
            depth += 1
        
        return result
            