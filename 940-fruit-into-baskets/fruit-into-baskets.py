class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        cnt = Counter()
        left = 0
        ans = 0

        for right, fruit in enumerate(fruits):
            cnt[fruit] += 1
            while left < right and len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1
            ans = max(ans, sum(cnt.values()))
        
        return ans