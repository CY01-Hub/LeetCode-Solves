class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        rsum = 0
        lsum = 0

        for n in nums:
            rsum += n

        for i in range(len(nums)):
            rsum -= nums[i]
            if rsum == lsum:
                return i
            lsum += nums[i]

        return -1
