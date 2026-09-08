class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        a = ""
        for i in s:
            if i != '-':
                a += i.upper()

        n = len(a)
        a = a[::-1]

        ans = ""
        for j in range(n):
            if j % k == 0:
                ans += '-'
            ans += a[j]

        ans = ans[::-1]
        m = len(ans)
        
        return ans[:m-1]
