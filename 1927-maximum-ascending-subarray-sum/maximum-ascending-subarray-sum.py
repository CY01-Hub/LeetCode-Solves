class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                currSum += nums[i]
            else:
                maxSum = max(maxSum, currSum)
                currSum = nums[i]

        maxSum = max(maxSum, currSum)
        return maxSum