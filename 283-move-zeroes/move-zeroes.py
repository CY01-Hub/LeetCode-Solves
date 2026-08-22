class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 0 or len(nums) == 1:
            return nums

        a = []
        c = 0
        for i in nums:
            if i != 0:
                a.append(i)
            else:
                c += 1
                
        for _ in range(c):
            a.append(0)

        nums[:] = a
        