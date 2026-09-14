class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        def heapify(nums: List[int], i:int, n:int):
            """
                max heap, funnel small values down
                - nums: array
                - i: the current index
                - n: the size of the heap 
            """

            left = (i << 1) + 1
            right = (i << 1) + 2
            largest = i

            if left < n and nums[left] > nums[largest]:
                largest = left
            
            if right < n and nums[right] > nums[largest]:
                largest = right
            
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                heapify(nums, largest, n)

        # build heap
        for i in range((n // 2) - 1, -1, -1):
            heapify(nums, i, n)
        
        for i in range(n):
            end = n - 1 - i
            nums[end], nums[0] = nums[0], nums[end]
            heapify(nums, 0, end)
        

        
        

                
        