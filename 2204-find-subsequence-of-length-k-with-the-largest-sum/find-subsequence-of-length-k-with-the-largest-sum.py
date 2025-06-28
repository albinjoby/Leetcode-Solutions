class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i],i) for i in range(len(nums))]
        heapq.heapify(heap)
        res = []
        while k:
            res.append(heapq.heappop(heap))
            k -= 1
        
        res.sort(key=lambda x: x[1])
        return [-item[0] for item in res]