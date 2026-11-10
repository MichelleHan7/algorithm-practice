class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ''
        i = 0
        min_length = inf
        for s in strs:
            min_length = min(min_length, len(s))
        while i < min_length:
            common = strs[0][i]
            for s in strs:
                if s[i] != common:
                    return ans
                else:
                    continue
            ans += common
            i += 1
        return ans