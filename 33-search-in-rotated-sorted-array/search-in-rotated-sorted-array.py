class Solution:
    def search(self, n: List[int], t: int) -> int:
        l, h = 0, len(n) - 1
        while l <= h:
            m = l + (h - l) // 2
            if n[m] == t:
                return m
            if n[l] <= n[m]:
                if n[l] <= t < n[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if n[m] < t <= n[h]:
                    l = m + 1
                else:
                    h = m - 1
        return -1