import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # since job order doesn't matter, heap stores # of cpu cycles on cooldown
        min_heap = []
        count = Counter(tasks)
        for task in count:
            for i in range(count[task]):
                min_heap.append(i*(n + 1))
        
        heapq.heapify(min_heap)
        
        cpu_cycle = 0
        while min_heap:
            if cpu_cycle >= min_heap[0]:
                heapq.heappop(min_heap)
            cpu_cycle += 1
        
        return cpu_cycle
        
        