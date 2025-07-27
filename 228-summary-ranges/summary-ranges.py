class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        res = []
        while i < len(nums):
            curr = nums[i]
            seq = str(curr)
            while i+1 < len(nums) and nums[i+1] == nums[i]+1:
                i += 1
            if nums[i] != curr:
                seq += "->" + str(nums[i])
            res.append(seq)
            i += 1
        return res