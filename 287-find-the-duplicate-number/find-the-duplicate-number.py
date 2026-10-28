class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            n = abs(nums[i])
            if nums[n] > 0 :
                nums[n] = -nums[n]
            else:
                ans = n
                break
        
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        
        return ans
