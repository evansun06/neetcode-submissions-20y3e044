import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        minheap = []
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for key in count:
            if len(minheap) < k:
                heapq.heappush(minheap, (count[key], key))
            else:
                heapq.heappushpop(minheap, (count[key], key))
        
        return [val for freq, val in minheap]

        