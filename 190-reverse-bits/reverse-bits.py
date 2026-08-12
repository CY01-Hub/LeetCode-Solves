class Solution:
    def reverseBits(self, n: int) -> int:
        a = 0
        for _ in range(32):
            b = n & 1
            a = (a << 1) | b
            n >>= 1
        return a