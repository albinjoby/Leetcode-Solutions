class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        left,right = nums[0],sum(nums[1:])
        for i in range(1,len(nums)):
            count += 1 if left >= right else 0
            right -= nums[i]
            left += nums[i]
        
        return count