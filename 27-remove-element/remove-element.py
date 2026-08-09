class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = []
        for i in nums:
            if i != val:
                x.append(i)
        nums[:] = x
        return len(x)