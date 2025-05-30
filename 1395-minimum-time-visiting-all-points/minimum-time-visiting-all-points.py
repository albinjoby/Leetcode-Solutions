class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        x1,y1 = points.pop(0)
        for x2,y2 in points:
            while not(x1 == x2) or not(y1 == y2):
                if x1 < x2:
                    x1 += 1
                elif x1 > x2:
                    x1 -= 1
                if y1 < y2:
                    y1 += 1
                elif y1 > y2:
                    y1 -= 1
                seconds += 1

        return seconds