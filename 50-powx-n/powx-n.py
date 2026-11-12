class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0: return 1
        if n == 1: return x
        mid = n // 2
        half = self.myPow(x, mid)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half