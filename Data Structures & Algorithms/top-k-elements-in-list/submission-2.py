import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        min_heap = []
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for num in counter:
            if len(min_heap) < k:
                heapq.heappush(min_heap, (counter[num], num))
            else:
                heapq.heappushpop(min_heap, (counter[num], num))
        return [tu[1] for tu in min_heap]

        