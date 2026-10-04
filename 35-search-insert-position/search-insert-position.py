class Solution:
    def searchInsert(self, n: List[int], t: int) -> int:
        if n[len(n) - 1] < t:
            return len(n)

        if n[0] > t:
            return 0
        
        s, e = 0, len(n) - 1
        while s <= e:
            m = s + ((e - s) // 2)
            if n[m] == t:
                return m
            elif n[m] < t:
                s = m + 1
            else:
                e = m - 1
        
        return s
