class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            if target - num in dic:
                return [idx,dic[target-num]]
            else:
                dic[num] = idx