class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # n edges
        ds = [-1] * (len(edges) + 1)

        def find(node: int) -> int:

            path = []
            while ds[node] >= 0:
                path.append(node)
                node = ds[node]
            
            for visited in path:
                ds[visited] = node
            
            return node

        def union(node_1, node_2):
            root_1 = find(node_1)
            root_2 = find(node_2)

            if -ds[root_1] >= -ds[root_2]:
                ds[root_1] += ds[root_2]
                ds[root_2] = root_1
            else:
                ds[root_2] += ds[root_1]
                ds[root_1] = root_2

        redundant_edge = edges[0]    

        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                redundant_edge = edge
            else:
                union(edge[0], edge[1])
        
        return redundant_edge

        


