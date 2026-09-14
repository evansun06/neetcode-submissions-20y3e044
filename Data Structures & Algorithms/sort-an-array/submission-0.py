import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        """
            heap sort. O(n) heapify | O(nlogn)heappop | O(1) space
        """

        maxheap = [-num for num in nums]
        heapq.heapify(maxheap)

        for i in range(len(nums) - 1, -1, -1):
            nums[i] = -heapq.heappop(maxheap)

        return nums