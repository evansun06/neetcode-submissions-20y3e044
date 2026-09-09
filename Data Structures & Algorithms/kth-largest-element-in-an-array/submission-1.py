import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            k-th largest - use a minheap

            minheap[0] gives us the k-th largest if len(minheap) == k

        """

        min_heap = []

        for num in nums:
            
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]


