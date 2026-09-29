class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        ans = []

        for i in range(len(matrix)):
            minimum = min(matrix[i])

            col = matrix[i].index(minimum)

            maximum = True

            for j in range(len(matrix)):
                if matrix[j][col] > minimum:
                    maximum = False
                    break

            if maximum:
                ans.append(minimum)

        return ans