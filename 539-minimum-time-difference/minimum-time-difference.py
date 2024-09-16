class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if timePoints.count(min(timePoints)) > 1:
            return 0

        for i in range(len(timePoints)):
            h,m = map(int,timePoints[i].split(":"))
            timePoints[i] = m+(h*60)

        timePoints.sort()
        res = 1440 - timePoints[-1] + timePoints[0]
        for i in range(1,len(timePoints)):
            diff = timePoints[i]-timePoints[i-1]
            res = min(res,diff)

        return res