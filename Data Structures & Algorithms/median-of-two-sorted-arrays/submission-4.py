class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = [] # shorter array
        B = [] # longer array
        lo = 0
        half = (len(nums1) + len(nums2)) // 2
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
            hi = len(nums1)
        else:
            A = nums2
            B = nums1
            hi = len(nums2)
            
        while lo <= hi:
            cut1 = (lo + hi) // 2
            cut2 = half - cut1

            A_left = A[cut1 - 1] if cut1 > 0 else float("-inf")
            A_right = A[cut1] if cut1 < len(A) else float("inf")

            B_left = B[cut2 - 1] if cut2 > 0 else float("-inf")
            B_right = B[cut2] if cut2 < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if (len(A) + len(B)) % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2 
                else:
                    return min(A_right, B_right)
            elif A_left > B_right:
                hi = cut1 - 1
            elif B_left > A_right:
                lo = cut1 + 1

