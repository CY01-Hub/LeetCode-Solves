class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = strs[0]
        for w in strs[1:]:
            while not w.startswith(p):
                p = p[:-1]

                if p == "":
                    return ""
        return p