class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dic:
                return [i,dic[val]]
            else:
                dic[nums[i]] = i

        