class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans = sorted(nums)
        Largest = ans[-1]
        Second = ans[-2]
        return (Largest - 1) * (Second - 1)