class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        q = deque()

        for i, num in enumerate(nums):
            # enter
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(i)
            # exit
            if i - q[0] + 1 > k:
                q.popleft()
            # append value to ans
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans