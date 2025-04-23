class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        i = 0
        while i < len(nums):
            if nums[i] == target:
                start = i
                while i < len(nums) and nums[i] == target:
                    i += 1
                end = i-1
            i += 1

        return [start,end]
