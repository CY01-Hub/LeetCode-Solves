class Solution:
    def diagonalSum(self, mat):
        total = 0

        for i in range(len(mat)):
            total += mat[i][i]
            
            if i != len(mat) - 1 - i:
                total += mat[i][len(mat) - 1 - i]

        return total
        