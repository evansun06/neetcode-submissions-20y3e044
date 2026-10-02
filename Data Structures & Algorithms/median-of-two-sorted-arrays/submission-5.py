class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        lenA = len(A)
        lenB = len(B)

        # Search the smaller array.
        if lenA > lenB:
            A, B = B, A
            lenA, lenB = lenB, lenA  # ADDED: lengths must also swap

        left, right = -1, lenA - 1  # CHANGED: -1 means take nothing from A
        half = (lenA + lenB) // 2

        while left <= right:
            midA = (left + right) // 2
            midB = half - midA - 2  # CHANGED: left count = (midA+1)+(midB+1)

            # ADDED: safely handle partitions at either end of an array
            Aleft = A[midA] if midA >= 0 else float("-inf")
            Aright = A[midA + 1] if midA + 1 < lenA else float("inf")
            Bleft = B[midB] if midB >= 0 else float("-inf")
            Bright = B[midB + 1] if midB + 1 < lenB else float("inf")

            if Aleft <= Bright and Bleft <= Aright:  # CHANGED: safe boundaries
                if (lenA + lenB) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2  # CHANGED
                else:
                    return min(Aright, Bright)  # CHANGED: safe boundaries
            elif Aleft > Bright:  # CHANGED: safe boundaries
                right = midA - 1  # CHANGED: take fewer elements from A
            else:
                left = midA + 1  # CHANGED: take more elements from A