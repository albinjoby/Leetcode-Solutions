class Solution(object):
    def findDuplicates(self, nums):
        res = []

        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                res.append(num)
            nums[num-1] = -nums[num-1]

        return res