class Solution:
    def sort(self, s):
        i = list(s)
        i.sort()
        return "".join(i)

    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        ans = {}
        for i in s:
            key = self.sort(i)
            if key in ans:
                ans[key].append(i)
            else:
                ans[key] = [i]
        return list(ans.values())