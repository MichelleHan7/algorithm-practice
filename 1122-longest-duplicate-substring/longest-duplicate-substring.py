class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def check(length):
            seen = set()
            for right in range(len(s)):
                if right - length + 1 >= 0:
                    sub = s[right - length + 1 : right + 1]
                    if sub in seen:
                        return sub
                    seen.add(sub)
            return ''

        left = 1
        right = len(s) - 1
        ans = ''
        while left <= right:
            mid = (left + right) // 2
            dup = check(mid)
            if dup:
                ans = dup
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
