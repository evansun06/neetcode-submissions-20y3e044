from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency_list = [[] for _ in range(n)]

        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
        
        visited = set()
        queue = deque([(0, -1)])

        while queue:

            curr, parent = queue.popleft()

            if curr in visited:
                return False

            visited.add(curr)

            for nxt in adjacency_list[curr]:
                if nxt == parent:
                    continue

                queue.append((nxt, curr))
        
        return True if len(visited) == n else False

            
