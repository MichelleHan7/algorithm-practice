class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        ans = ''
        for i in range(len(s)):
            if len(expand(i, i+1)) > len(ans):
                ans = expand(i, i+1)
            if len(expand(i, i)) > len(ans):
                ans = expand(i, i)
        return ans