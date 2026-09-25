class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_list = sorted(nums1 + nums2)
        l = len(merged_list)
        if l % 2 == 0:
            mid1 = merged_list[l // 2 - 1]
            mid2 = merged_list[l // 2]
            return (mid1 + mid2) / 2
        else:
            return float(merged_list[l // 2])