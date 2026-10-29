class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        ans = ""
        for i in range(len(lst)-1, -1, -1):
            ans += lst[i] + " "
        return ans.strip()