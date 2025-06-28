class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i],i) for i in range(len(nums))]
        heapq.heapify(heap)
        res = [heapq.heappop(heap) for _ in range(k)]
        res.sort(key=lambda x: x[1])
        return [-i for i,_ in res]