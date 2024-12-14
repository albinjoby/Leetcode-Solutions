class Solution(object):
    def pickGifts(self, gifts, k):
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            val = -heapq.heappop(max_heap)
            val = floor(sqrt(val))
            heapq.heappush(max_heap, -val)

        return int(-sum(max_heap))
