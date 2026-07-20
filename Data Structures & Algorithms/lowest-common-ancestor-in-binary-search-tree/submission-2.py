# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # recursion solution
        def _dfs(node: TreeNode) -> TreeNode:
            if node is None:
                return None
            if (p.val <= node.val and q.val >= node.val) or (q.val <= node.val and p.val >= node.val):
                return node
            else:
                return (_dfs(node.left) or _dfs(node.right))
        

        return _dfs(root)