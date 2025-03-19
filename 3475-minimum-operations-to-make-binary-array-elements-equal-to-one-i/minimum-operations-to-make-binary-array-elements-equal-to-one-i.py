class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l,c,r = 0,1,2
        count = 0
        while r<len(nums):
            if nums[l] == 0:
                nums[l] = 1
                nums[c] ^= 1
                nums[r] ^= 1
                count += 1
            r += 1
            c += 1
            l += 1

        if nums.count(0) == 0:
            return count
        return -1