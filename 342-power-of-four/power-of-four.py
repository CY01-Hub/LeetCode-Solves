class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in range(1000000000000000000000000):
            if (4 ** i) == n:
                return True
            elif (4 ** i) > n:
                break 
        return False
