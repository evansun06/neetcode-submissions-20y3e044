import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []

        result = []
        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))

            
            if (right + 1 >= k):
                while max_heap[0][1] > right or max_heap[0][1] < right - k + 1:
                    heapq.heappop(max_heap)

                result.append(-1 * max_heap[0][0])

                if nums[right - k + 1] == (-1 * max_heap[0]):
                    heapq.heappop(max_heap)

        return result
