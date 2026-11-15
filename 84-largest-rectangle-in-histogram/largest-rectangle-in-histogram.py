class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        ans = 0
        st = [] # index, height

        for i, h in enumerate(heights):
            start = i
            while st and h < st[-1][1]:
                index, height = st.pop()
                ans = max(ans, height * (i - index))
                start = index
            st.append((start, h))
        
        for i, h in st:
            ans = max(ans, h * (len(heights) - i))
        return ans
