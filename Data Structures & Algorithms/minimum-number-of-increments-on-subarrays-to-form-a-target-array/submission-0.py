from collections import defaultdict
import heapq
import bisect

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        indice_map = defaultdict(list)

        for i in range(len(target)):
            indice_map[target[i]].append(i)

        maxheap = []

        for value in indice_map:
            heapq.heappush(maxheap, (-value, indice_map[value]))

        operations = 0

        while maxheap:
            value, indices = heapq.heappop(maxheap)
            value = -value

            if value == 0:
                break

            indices = set(indices)

            
            if maxheap and -maxheap[0][0] == value - 1:
                for num in indices:
                    if num - 1 not in indices:
                        operations += 1

                    bisect.insort(maxheap[0][1], num)

            else:
                for num in indices:
                    if num - 1 not in indices:
                        operations += 1

                
                heapq.heappush(maxheap, (-(value - 1), sorted(indices)))

        return operations