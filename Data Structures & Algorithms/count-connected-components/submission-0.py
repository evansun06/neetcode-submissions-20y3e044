class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        class disjointSet:

            def __init__(self, n):
                self.array = [-1] * n
                self.num_sets = n
            
            def union(self, a, b):
                if self.same_set(a, b):
                    return

                root_a = self.get_rep(a)
                root_b = self.get_rep(b)

                if self.get_size(a) > self.get_size(b):
                    self.array[root_a] += self.array[root_b]
                    self.array[root_b] = root_a
                else:
                    self.array[root_b] += self.array[root_a]
                    self.array[root_a] = root_b

                self.num_sets -= 1

            def same_set(self, a, b):
                return self.get_rep(b) == self.get_rep(a)
            
            def get_rep(self, a):

                path = []
                
                def search(num):
                    if self.array[num] >= 0:
                        path.append(num)
                        return search(self.array[num])
                    else:
                        for n in path:
                            self.array[n] = num

                        return num

                return search(a)

            def get_size(self, a):
                root = self.get_rep(a)
                return -self.array[root]

        ds = disjointSet(n)

        for a, b in edges:
            ds.union(a, b)
        
        return ds.num_sets
            

        