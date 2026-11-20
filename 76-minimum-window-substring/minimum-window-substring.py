class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        cnt_t = Counter(t)
        cnt_s = Counter()
        ans_left, ans_right = -1, m
        left = 0

        for right, char in enumerate(s):
            cnt_s[char] += 1
            while cnt_s >= cnt_t:
                if right - left <= ans_right - ans_left:
                    ans_right, ans_left = right, left
                cnt_s[s[left]] -= 1
                left += 1
        
        if ans_left == -1:
            return ''
        else:
            return s[ans_left:ans_right+1]