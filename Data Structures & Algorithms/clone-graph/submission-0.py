"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        cloned_nodes = {}

        visited = set()

    
        def dfs(node):
            
            if node in visited:
                return
            else:
                visited.add(node)

                cloned = None

                if node.val in cloned_nodes:
                    cloned = cloned_nodes[node.val]
                else:
                    cloned = Node(node.val)
                    cloned_nodes[node.val] = cloned

                for n in node.neighbors:

                    dfs(n)

                    if n.val not in cloned_nodes:
                        cloned_nodes[n.val] = Node(n.val)

                    cloned.neighbors.append(cloned_nodes[n.val])

        dfs(node)
        
        return cloned_nodes[1] if 1 in cloned_nodes else None
