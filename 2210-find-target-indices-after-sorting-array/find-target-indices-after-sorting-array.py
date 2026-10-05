class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n, c = 0, 0
        for i in nums:
            if i == target:
                c += 1
            elif i < target:
                n += 1
        
        ans = []
        while c > 0:
            ans.append(n)
            n += 1
            c -=1
        
        return ans