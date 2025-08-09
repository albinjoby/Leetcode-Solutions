class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math, heapq
        heap = []
        for x2,y2 in points:
            rank = math.sqrt(((0-x2)**2)+(((0-y2)**2)))
            heapq.heappush(heap, (rank, [x2,y2]))
        
        return [heapq.heappop(heap)[-1] for _ in range(k)]
        