class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        ans = [0] * n
        st = []

        for i in range(n-1, -1, -1):
            h = heights[i]
            while st and h > heights[st[-1]]:
                ans[i] += 1
                st.pop()
            if st:
                ans[i] += 1
            st.append(i)
        
        return ans