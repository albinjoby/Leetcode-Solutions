class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        cost = 0
        import heapq
        heap = [(0,0)]

        while len(seen) < len(points):
            dist, i = heapq.heappop(heap)
            if i in seen:
                continue
            seen.add(i)
            cost += dist
            x1,y1 = points[i]

            for j in range(len(points)):
                if j not in seen:
                    x2, y2 = points[j] 
                    dist = abs(x2-x1) + abs(y2-y1)
                    heapq.heappush(heap, (dist,j))

        return cost
