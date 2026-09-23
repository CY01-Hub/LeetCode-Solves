class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        st = 0
        nd = 1
        rd = 1

        for _ in range(n):
          th = st + nd + rd
          st = nd
          nd = rd
          rd = th

        return st