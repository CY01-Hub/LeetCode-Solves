class Solution:
    def merge(self, merged_list, low, mid, high):
        temp = []
        i = low
        j = mid + 1

        while i <= mid and j <= high:
            if merged_list[i] <= merged_list[j]:
                temp.append(merged_list[i])
                i += 1
            else:
                temp.append(merged_list[j])
                j += 1
        
        while i <= mid:
            temp.append(merged_list[i])
            i += 1

        while j <= high:
            temp.append(merged_list[j])
            j += 1

        merged_list[low:high+1] = temp
    
    def mergesort(self, merged_list, low, high):
        if low < high:
            mid = low + ((high - low) // 2)
            self.mergesort(merged_list, low, mid)
            self.mergesort(merged_list, mid + 1, high)
            self.merge(merged_list, low, mid, high)

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_list = []
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 == 0 and l2 == 0:
            return False

        for i in range(l1):
            merged_list.append(nums1[i])

        for j in range(l2):
            merged_list.append(nums2[j])

        s = len(merged_list)
        self.mergesort(merged_list, 0, s - 1)

        if s % 2 != 0:
            return float(merged_list[s // 2])
        else:
            return (float(merged_list[s // 2]) + float(merged_list[s // 2 - 1])) / 2
        