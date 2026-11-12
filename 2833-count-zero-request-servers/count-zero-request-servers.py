class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda p:p[1])
        sorted_queries = sorted(enumerate(queries), key=lambda q:q[1])

        cnt = defaultdict(int)
        ans = [0] * len(queries)

        left = right = 0

        for i, q in sorted_queries:
            while right < len(logs) and logs[right][1] <= q:
                server_id = logs[right][0]
                cnt[server_id] += 1
                right += 1

            # Shrink the window
            while left < right and logs[left][1] < q - x:
                server_id = logs[left][0]
                cnt[server_id] -= 1

                if cnt[server_id] == 0:
                    del cnt[server_id]

                left += 1

            ans[i] = n - len(cnt)

        return ans
