class Solution:
    def minCost(self, colors: str, time: List[int]) -> int:
        res = 0
        for i in range(1,len(colors)):
            if colors[i-1] == colors[i]:
                res += min(time[i-1],time[i])
                time[i] = max(time[i-1],time[i])

        return res