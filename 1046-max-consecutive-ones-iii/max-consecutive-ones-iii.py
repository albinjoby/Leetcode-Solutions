class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        res = 0
        l, x = 0, 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
            else:
                x += 1
                while x > k:
                    if nums[l] == 1:
                        count -= 1
                    else:
                        x -= 1
                    l += 1
            res = max(res, count+x)
        
        return res