class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        cnt = Counter(s)
        ans = []
        length = 0
        cur_car = set()
        for i, c in enumerate(s):
            cnt[c] -= 1
            cur_car.add(c)
            length += 1
            if cnt[c] == 0:
                cur_car.remove(c)
            if len(cur_car) == 0:
                ans.append(length)
                length = 0
        return ans


