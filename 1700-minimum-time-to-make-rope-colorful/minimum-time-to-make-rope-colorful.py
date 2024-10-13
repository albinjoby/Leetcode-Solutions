class Solution:
    def minCost(self, colors: str, time: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1,len(colors)):
            if colors[l] == colors[r]:
                if time[l] < time[r]:
                    res += time[l]
                    l = r
                else:
                    res += time[r]
            else:
                l = r

        return res