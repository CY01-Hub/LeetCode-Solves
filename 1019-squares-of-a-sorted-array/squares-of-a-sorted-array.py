class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        st = 0
        end = len(nums) - 1
        ptr = len(nums) - 1 

        while st <= end:
            ss = nums[st] * nums[st]
            es = nums[end] * nums[end]

            if ss >= es:
                ans[ptr] = ss
                st += 1
            else:
                ans[ptr] = es
                end -= 1

            ptr -= 1
            
        return ans