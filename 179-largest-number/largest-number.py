class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if int(str(nums[j])+str(nums[i])) > int(str(nums[i])+str(nums[j])):
                    nums[i],nums[j] = nums[j],nums[i]

        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        res = ''.join(nums)

        return res if res[0] != '0' else '0'