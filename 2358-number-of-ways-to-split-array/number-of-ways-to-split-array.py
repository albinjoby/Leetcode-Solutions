class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        left,right = nums[0],sum(nums[1:])
        for i in range(1,len(nums)):
            if left >= right:
                count += 1
            right -= nums[i]
            left += nums[i]
        
        return count