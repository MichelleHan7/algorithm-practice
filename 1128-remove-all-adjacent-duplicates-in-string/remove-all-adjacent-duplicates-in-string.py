class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []

        for i, ch in enumerate(s):
            if st and st[-1] == ch:
                st.pop()
            else:
                st.append(ch)
        return ''.join(st)