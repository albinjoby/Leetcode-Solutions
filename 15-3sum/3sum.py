class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif target > 0:
                    r -= 1
                else:
                    l += 1
            
        return list(res)