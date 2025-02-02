class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i:]+nums[:i] == sorted_nums:
                return True
        
        return False