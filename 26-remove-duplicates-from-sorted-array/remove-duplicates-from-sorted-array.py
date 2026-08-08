class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        start = 0
        for i in range(1, size):
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i]
        return len(nums[:start+1])
