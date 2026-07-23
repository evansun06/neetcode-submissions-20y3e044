# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node: TreeNode):
            nonlocal result

            if node is None:
                result.append("N")
            else:
                result.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return ",".join(result)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        _data = data.split(",")
       

        def dfs():
            if _data[self.i] == "N":
                self.i += 1
                return None
            else:
                node = TreeNode(int(_data[self.i]))
                self.i +=1
                node.left = dfs()
                node.right = dfs()
                return node
        
        return dfs()
            



