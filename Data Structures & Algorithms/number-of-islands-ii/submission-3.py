class disjointSet:
    """
    if parent[cell] = cell, cell is a root
    """
    def __init__(self):
        self.parents = {}
        self.size = {}

    def add_cell(self, cell: tuple[int]):
        if cell not in self.parents:
            self.parents[cell] = cell
            self.size[cell] = 1
    
    def find(self, cell: tuple[int]):
        while self.parents[cell] != cell:
            self.parents[cell] = self.parents[self.parents[cell]]
            cell = self.parents[cell]
        return cell

    def union(self, cell1: tuple[int], cell2: tuple[int]):
        root1, root2 = self.find(cell1), self.find(cell2)

        if root1 == root2:
            return False
        
        if self.size[root1] >= self.size[root2]:
            self.parents[root2] = root1
            self.size[root1] += self.size[root2]
            self.size[root2] = 0
        else:
            self.parents[root1] = root2
            self.size[root2] += self.size[root1]
            self.size[root1] = 0
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        """
        Iterate through positions and apply each island:
        - then count the number of islands (bfs) O(n^2)
        
        count = 0 

        For each island we add:
         + 1 
         - 1 for every horizontal/vertical neighbor that is island

         [1,1,1]
         [0,1,1]
         [0,0,0]
         count = 1
         {(0,0), (0,1), (0,2), (1,2), (1,1)}
        """

        dsu = disjointSet()

        count = 0
        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]

        res = []

        for row, col in positions:
            

            if (row,col) in dsu.parents:
                res.append(count)
                continue

            count += 1
            dsu.add_cell((row, col))

            for dr, dc in directions:
                adj_row, adj_col = row + dr, col + dc

                if (adj_row, adj_col) in dsu.parents and dsu.union((row,col), (adj_row, adj_col)):
                    count -= 1
            res.append(count)
        return res
            





            


        