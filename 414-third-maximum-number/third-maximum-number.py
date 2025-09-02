class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        if len(set(nums)) < 3:
            return max(list(set(nums)))
        
        nums = list(set(nums))
        nums = [-num for num in nums]
        heapq.heapify(nums)
        print(nums)
        for i in range(3):
            res = heapq.heappop(nums)
        return -res