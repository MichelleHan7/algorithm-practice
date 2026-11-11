class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            level = [1] * (i+1)
            for j in range(1, i):
                level[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(level)
        return ans


