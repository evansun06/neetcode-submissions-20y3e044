# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 

        def _dfs(node: TreeNode, path: list[int]):
            nonlocal count

            if node is None:
                return
            else:
                

                if all(node.val >= value for value in path):
                    count +=1

                path.append(node.val)
                
                _dfs(node.left, path)
                _dfs(node.right, path)

                path.pop()
        
        _dfs(root, [])

        return count
