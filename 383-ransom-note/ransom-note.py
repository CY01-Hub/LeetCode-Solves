from collections import Counter
class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        x = Counter(r)
        y = Counter(m)

        for i in x:
            if x[i] > y[i]:
                return False

        return True        