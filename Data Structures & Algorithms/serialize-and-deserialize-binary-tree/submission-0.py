# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    #           [1]
    #        [2]    [3]
    #      [3]  n  [4] n
    #
    # [1, 2, 3, 3, n, 4, n, n, n, n, n]
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        q = collections.deque()
        q.append(root)
        result = [str(root.val)]

        while q:
            nxt = q.popleft()
            if nxt.left:
                q.append(nxt.left)
                result.append(str(nxt.left.val))
            else:
                result.append("null")

            if nxt.right:
                q.append(nxt.right)
                result.append(str(nxt.right.val))
            else:
                result.append("null")
        
        return ",".join(result)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        _data = data.split(",")
        nodes = [TreeNode(val) if val != "null" else None for val in _data]

        q = collections.deque()
        q.append(nodes[0])
        index = 1

        while q:
            node = q.popleft()

            if nodes[index] is not None:
                q.append(nodes[index])
            node.left = nodes[index]
            index += 1

            if nodes[index] is not None:
                q.append(nodes[index])
            node.right = nodes[index]
            index += 1

        return nodes[0]
            



