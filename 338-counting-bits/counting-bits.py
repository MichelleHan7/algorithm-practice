class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n+1)

        for num in range(1, n+1):
            count = 0
            for i in range(32):
                if (1<<i) & num:
                    count += 1
            ans[num] = count
        
        return ans
