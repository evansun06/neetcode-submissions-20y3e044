class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        take the largest value from nums2 and bubble it down nums1
        """


        insert_at = m
        for i in range(n):
            j = insert_at
            nums1[j] = nums2[i]
            while j > 0:
                if nums1[j] < nums1[j - 1]:
                    nums1[j], nums1[j - 1], = nums1[j-1], nums1[j]
                    j -= 1
                else:
                    break
            insert_at += 1

            

        