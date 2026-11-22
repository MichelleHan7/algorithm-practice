class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxside = 0

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            maxside = max(maxside, dp[i][0])

        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            maxside = max(maxside, dp[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(
                        dp[i-1][j-1],
                        dp[i][j-1],
                        dp[i-1][j]
                    )
                    maxside = max(maxside, dp[i][j])

        return maxside ** 2