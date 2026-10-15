class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {c: i for i, c in enumerate(s)}
        ans = []
        start = end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                ans.append(end-start+1)
                start = end+1

        return ans