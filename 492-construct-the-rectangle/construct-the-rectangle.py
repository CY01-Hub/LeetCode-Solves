class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a = int(area ** 0.5)

        while area % a != 0:
            a -= 1

        return [area // a, a]
        