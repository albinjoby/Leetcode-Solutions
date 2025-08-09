class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k:
            val = heapq.heappop(nums)
            k -= 1
        return -val