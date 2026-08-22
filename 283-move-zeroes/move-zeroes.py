class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 0 or len(nums) == 1:
            return nums

        ans = []
        count = 0
        for i in nums:
            if i != 0:
                ans.append(i)
            else:
                count += 1
                
        for _ in range(count):
            ans.append(0)

        nums[:] = ans
        