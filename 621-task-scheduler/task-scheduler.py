class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        cnt = Counter(tasks)
        count = [-c for c in cnt.values()]
        heapq.heapify(count) # 可以被用来安排的

        time = 0
        q = deque() # 现在安排不了的，之后可以被放回heap的

        while q or count:
            time += 1
            if count:
                new_count = 1 + heapq.heappop(count)
                if new_count:
                    q.append([new_count, time + n])
            if q and q[0][1] == time: 
                c, t = q.popleft()
                heapq.heappush(count, c)
        
        return time



        