class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        res = ""
        count = float('-inf')
        if len(nums) < 3:
            return res
        for i in range(len(nums)-2):
            if nums[i] == nums[i+1] == nums[i+2]:
                if (int(nums[i])*3) > count:
                    res = nums[i:i+3]
                    count = int(nums[i])*3
            
        return res