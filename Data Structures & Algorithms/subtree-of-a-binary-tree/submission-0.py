# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        exists = False
        def isIdentical(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            if n1 is None and n2 is None:
                return True
            else:
                if (n1 is None and n2 is not None) or (n2 is None and n1 is not None):
                    return False
                else:
                    if n1.val == n2.val:
                        return isIdentical(n1.left, n2.left) and isIdentical(n1.right, n2.right)
                    else:
                        return False
        
        def dfs(node: Optional[TreeNode]):
            nonlocal exists
            if node is None:
                return
            else:
                if isIdentical(node, subRoot):
                    exists = True
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return exists