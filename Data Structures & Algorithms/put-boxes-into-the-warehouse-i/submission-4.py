class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)

        clearance = warehouse[0]
        for i in range(len(warehouse)):
            clearance = min(clearance, warehouse[i])
            warehouse[i] = clearance

        count = 0

        for i in range(len(warehouse) - 1, -1, -1):
            if not boxes:
                break
            elif boxes[-1] <= warehouse[i]:
                count += 1
                boxes.pop()

        
        return count