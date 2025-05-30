class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = {}
        l = len(nums)
        m = max(nums)
        counter = Counter(nums)
        vals = set(nums)
        for n in range(m,0-1,-1):
            if n not in vals:
                continue
            l -= (counter[n])
            res[n] = l
        for i in range(len(nums)):
            nums[i] = res[nums[i]]
        return nums
        