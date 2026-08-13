class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x, y = [], []

        for i in list(s):
            if i != "#":
                x.append(i)
            else:
                if x:
                    x.pop()

        for j in list(t):
            if j != "#":
                y.append(j)
            else:
                if y:
                    y.pop()

        return True if x == y else False