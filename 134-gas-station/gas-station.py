class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diff = [gas[i] - cost[i] for i in range(len(gas))]

        res = 0
        total = 0
        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                total = 0
                res = i+1
            
        return res