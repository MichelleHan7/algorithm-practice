class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        left = 0
        cnt2 = Counter()
        for right, c in enumerate(s2):
            cnt2[c] += 1
            if right - left + 1 > len(s1):
                cnt2[s2[left]] -= 1
                left += 1
            if cnt2 == cnt:
                return True
        return False