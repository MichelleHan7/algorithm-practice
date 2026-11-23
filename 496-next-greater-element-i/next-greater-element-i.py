class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        m = len(nums2)
        ans = [-1] * n
        st= []

        for i in range(n):
            for j in range(m-1, -1, -1):
                n = nums2[j]
                while st and st[-1] <= nums2[j]:
                    st.pop()
                if n == nums1[i] and st:
                    ans[i] = st[-1]
                st.append(nums2[j])
            st = []
        return ans