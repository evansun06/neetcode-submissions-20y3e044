class Solution:
    def numIslands2(
        self, m: int, n: int, positions: List[List[int]]
    ) -> List[int]:
        parent = {}
        size = {}
        count = 0
        result = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def find(cell):
            while cell != parent[cell]:
                parent[cell] = parent[parent[cell]]
                cell = parent[cell]
            return cell

        def union(a, b):
            root_a, root_b = find(a), find(b)

            if root_a == root_b:
                return False

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]
            return True

        for row, col in positions:
            cell = (row, col)

            if cell in parent:
                result.append(count)
                continue

            parent[cell] = cell
            size[cell] = 1
            count += 1

            for dr, dc in directions:
                neighbor = (row + dr, col + dc)

                if neighbor in parent and union(cell, neighbor):
                    count -= 1

            result.append(count)

        return result