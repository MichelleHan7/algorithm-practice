class Solution:

    def __init__(self, w: list[int]):
        self.weights = w
        self.prob = [0] * len(self.weights)
        total = sum(self.weights)
        self.prob[0] = self.weights[0] / total
        for i in range(1, len(self.weights)):
            self.prob[i] = self.prob[i-1] + self.weights[i] / total
 
    def pickIndex(self) -> int:
        num = random.random()
        left = 0
        right = len(self.weights)-1
        while left <= right:
            mid = (left + right) // 2
            if self.prob[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()