class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        nodes from 1 to n
        n edges that form a cycle in the connected graph
        return the edge that can be removed so that the graph is acyclic (return last)

        """

        dsj = DisjointSet(len(edges))

        for edge in edges:
            if dsj.union(edge[0], edge[1]) == False:
                return edge
            



class DisjointSet:
    """
    if parents[i] < 0 we have found the representative index i
    and i * -1 is the size

    we can do path compression on find by maintaining a visited list 
    and setting their representative to the root.
    """

    def __init__(self, n):
        self.parents = [-1] * (n + 1)
    
    def find(self, key):
        visited = []
        i = key
        while self.parents[i] >= 0:
            visited.append(i)
            i = self.parents[i]
        
        for visited_key in visited:
            self.parents[visited_key] = i
        
        return i
    
    def union(self, set1, set2) -> bool:
        root1, root2 = self.find(set1), self.find(set2)

        if root1 == root2:
            return False

        size1, size2 = -self.parents[root1], -self.parents[root2]

        if size1 >= size2:
            self.parents[root1] += self.parents[root2]
            self.parents[root2] = root1
        else:
            self.parents[root2] += self.parents[root1]
            self.parents[root1] = root2

        return True