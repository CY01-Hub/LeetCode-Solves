class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        before = max(nums)
        twice = []
        for i in nums:
            if i == before:
                twice.append(i)
            else:
                twice.append(i * 2)
        after = max(twice)
        if before == after:
            return nums.index(before)
        else:
            return -1
