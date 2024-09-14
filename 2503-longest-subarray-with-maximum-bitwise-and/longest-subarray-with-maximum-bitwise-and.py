class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        highest,count = 1,0
        for num in nums:
            if num == target:
                count += 1
            else:
                count = 0
            highest = max(highest,count)

        return highest