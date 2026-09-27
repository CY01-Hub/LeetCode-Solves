class Solution:
    def maxArea(self, height: list[int]) -> int:
        st, end = 0, len(height) - 1
        maxCap = 0

        while st < end:
            lnt = min(height[st], height[end])
            wid = end - st

            currCap = lnt * wid
            maxCap = max(currCap, maxCap)

            if height[st] < height[end]:
                st += 1
            else:
                end -= 1
        
        return maxCap
