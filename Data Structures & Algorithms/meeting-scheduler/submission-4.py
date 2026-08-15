class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        i = 0
        j = 0
        slots1.sort(key = lambda slot: slot[0])
        slots2.sort(key = lambda slot: slot[0])

        while i < len(slots1) and j < len(slots2):
            start_1, end_1 = slots1[i]
            start_2, end_2 = slots2[j]
            overlap_start = max(start_1, start_2)
            overlap_end = min(end_1, end_2)

            if overlap_end - overlap_start >= duration:
                return [overlap_start, overlap_start + duration]
            
        
            if end_1 <= end_2:
                i += 1
            else:
                j += 1
        
        return []

