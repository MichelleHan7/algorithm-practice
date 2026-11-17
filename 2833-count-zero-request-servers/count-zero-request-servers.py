class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda p: p[1])
        sorted_queries = sorted(enumerate(queries), key=lambda p: p[1])
        
        l = len(queries)
        ans = [0] * l
        freq = defaultdict(int)
        left = right = 0
        active = 0
        for i, q in sorted_queries:
            # Add logs with time <= q
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                freq[server] += 1
                if freq[server] == 1:
                    active += 1

                right += 1

            # Remove logs with time < q - x
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]

                freq[server] -= 1
                if freq[server] == 0:
                    active -= 1

                left += 1

            ans[i] = n - active

        return ans
