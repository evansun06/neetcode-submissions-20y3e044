from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        n = 2
        tasks = [A, A, B]

        AB_A
        BA__A
        """

        counter = {}

        for task in tasks:
            if task in counter:
                counter[task] += 1
            else:
                counter[task] = 1
        

        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)

        q = deque()
        cycle = 0
        while max_heap or q:
   

            if max_heap:
                count = -heapq.heappop(max_heap)
                count -= 1

                if count > 0:
                    q.append((count, cycle + n + 1))
        
            cycle += 1

            if q and q[0][1] == cycle:
                count, _ = q.popleft()
                heapq.heappush(max_heap, -count)

        return cycle


