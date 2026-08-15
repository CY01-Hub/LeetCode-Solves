class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        for char in set(r):
            if r.count(char) > m.count(char):
                return False
        return True      