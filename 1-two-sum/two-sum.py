class Solution(object):
    def twoSum(self, nums, target):
        num = []
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                if (nums[a] + nums[b]) == target:
                    num.append(a)
                    num.append(b)
        return num