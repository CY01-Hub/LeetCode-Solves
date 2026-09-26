class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1] * n
        product = 1

        for i in range(n-1, -1, -1):
            product *= nums[i]
            right[i] = product

        ans = [1] * n
        left = 1

        for i in range(n - 1):
            val = left * right[i + 1]
            ans[i] = val
            left *= nums[i]
        ans[n - 1] = left
        
        return ans
