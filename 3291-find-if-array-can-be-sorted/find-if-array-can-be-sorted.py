class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        res = nums.copy()
        dic = {num: bin(num)[2:].count('1') for num in nums}
        
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1] and dic[nums[j]] == dic[nums[j+1]]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        res.sort()
        return nums == res