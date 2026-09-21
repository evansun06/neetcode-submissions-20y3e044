from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        bfs
        """
        dead = set()
        visited = set()
        target = (int)(target)

        target = (
            (target // 1000) % 10,
            (target // 100) % 10,
            (target // 10) % 10,
            target % 10
        )

        for combos in deadends:
            combos = (int)(combos)
            dead.add(
                (
                    (combos // 1000) % 10,
                    (combos // 100) % 10,
                    (combos // 10) % 10,
                    combos % 10
                )
            )

        start = (0, 0, 0, 0)
        if start in dead:
            return -1

        q = deque([start])
        visited = {start}
        moves = 0

        while q:
            for _ in range(len(q)):
                candidate = q.popleft()

                if candidate == target:
                    return moves

                for i, lock in enumerate(candidate):
                    for change in (1, -1):
                        neighbor = list(candidate)
                        neighbor[i] = (lock + change) % 10
                        neighbor = tuple(neighbor)

                        if neighbor in visited or neighbor in dead:
                            continue

                        q.append(neighbor)
                        visited.add(neighbor)

            moves += 1

        return -1

            
            

                    
            