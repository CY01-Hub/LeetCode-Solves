class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        st, nd, rd = max(nums), max(nums), max(nums)

        for i in range(len(nums)):
            ele = nums[i]
            if st >= ele:
                st = ele
            elif nd >= ele:
                nd = ele
            else:
                rd = ele
                return True
        
        return False