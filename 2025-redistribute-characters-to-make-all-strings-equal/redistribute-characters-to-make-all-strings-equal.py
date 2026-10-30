class Solution:
    def makeEqual(self, w: list[str]) -> bool:
        return all(''.join(w).count(ch) % len(w) == 0 for ch in set(''.join(w)))
        