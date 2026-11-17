class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2
            time = 0
            count = 0
            for w in weights:
                if count + w <= mid:
                    count += w
                else:
                    time += 1
                    count = w
            if count:
                time += 1
            if time > days:
                left = mid + 1
            else:
                right = mid - 1
        
        return left