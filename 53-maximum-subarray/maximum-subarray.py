class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            res = max(res, nums[i])
        return res
        
        # total = 0
        # res = float('-inf')
        # for num in nums:
        #     total += num
        #     res = max(res, total)

        #     if total < 0:
        #         total = 0

        # return res
