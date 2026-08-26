class Solution:
    def addStrings(self, n1: str, n2: str) -> str:
        a = len(n1) - 1
        b = len(n2) - 1
        c = 0
        ans = ""

        while a >= 0 or b >= 0 or c:
            x = int(n1[a]) if a >= 0 else 0
            y = int(n2[b]) if b >= 0 else 0

            t = x + y + c

            ans += str(t % 10)
            c = t // 10

            a -= 1
            b -= 1
        
        return ans[::-1]