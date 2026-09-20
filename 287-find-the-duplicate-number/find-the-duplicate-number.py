class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n=len(nums)
        check = [False]*(n+1)
        for n in nums:
            if check[n]:
                return n
            check[n]=True
        return -1