class Solution:
    def minSubArrayLen(self, t: int, arr: List[int]) -> int:
        l = 0
        total = 0
        res = float('inf')

        for r in range(len(arr)):
            total += arr[r]

            while total >= t:
                res = min(res, r-l+1)
                total -= arr[l]
                l += 1

        if res == float('inf'):
            return 0
        else:
            return res