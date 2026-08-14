class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        class disjointSet:
            # O(1) find(i) -> representative index
            # O(1) size(i) -> size
            # O(1) union 

            # uptree style 

            def __init__(self, n: int):
                # every node begins in its own group
                self.array = [-1] * n
                self.set_count = n
            
            def find(self, node: int) -> int:
                # for O(1) amortized, we need to implement self healing

                path = []

                while self.array[node] >= 0:
                    path.append(node)
                    node = self.array[node] 
                    
                for visited in path:
                    self.array[visited] = node

                return node
                
            def size(self, node: int) -> int:
                return -self.array[self.find(node)]


            def union(self, node_1: int, node_2: int) -> int:

                if self.find(node_1) == self.find(node_2):
                    return

                root_1 = self.find(node_1)
                root_2 = self.find(node_2)

                if self.size(root_1) >= self.size(root_2):
                    self.array[root_1] += self.array[root_2]
                    self.array[root_2] = root_1
                else:
                    self.array[root_2] += self.array[root_1]
                    self.array[root_1] = root_2

                self.set_count -= 1
            
        ds = disjointSet(n)

        for node_1, node_2 in edges:
            ds.union(node_1, node_2)

        return ds.set_count


                



                


