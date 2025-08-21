class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum = nums[0]
        maxsum = nums[0]
        for num in nums[1:]:
            currentsum = max(num,currentsum+num)
            maxsum = max(currentsum,maxsum)
        return maxsum















        # res = 0
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     j = i + 1
        #     while curr > 0 and j < len(nums):
        #         curr += nums[j]
        #         j += 1
        #     res = max(res, curr)
        # print(res)
            