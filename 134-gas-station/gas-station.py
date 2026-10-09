class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1
        ans = 0
        remain = 0
        for i in range(len(gas)):
            remain += gas[i] - cost[i]
            if remain < 0:
                remain = 0
                ans = i + 1
        return ans