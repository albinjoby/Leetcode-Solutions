class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 1
        for i in range(1,len(nums)):
            num = nums[i]
            if count <= 0:
                res = nums[i]
            if num == res:
                count += 1
            else:
                count -= 1
            print(res, count)

        return res