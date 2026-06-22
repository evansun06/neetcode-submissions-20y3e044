class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # num1_l
        # num1_r
        # num2_l
        # num2_r
        # mid = len(num1) 
        # while (num1_r + num2_r) >= (num1_l + num2_l):

        i = 0
        j = 0
        merged = []
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                merged.append(nums2[j])
                j += 1
            elif j == len(nums2):
                merged.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        if (len(nums1) + len(nums2)) % 2 == 0:
            right = merged[(len(nums1) + len(nums2)) // 2]
            left = merged[((len(nums1) + len(nums2)) // 2) - 1]
            return (float(left) + float(right)) / 2
        else:
            return float(merged[((len(nums1) + len(nums2))// 2)])

