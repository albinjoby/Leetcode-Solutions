class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        val = max(nums)
        l = 0
        count, res = 0, 0
        for r in range(len(nums)):
            if nums[r] == val:
                count += 1

            while count > k:
                count -= 1 if nums[l] == val else 0
                l += 1

            while count == k and nums[l] != val:
                count -= 1 if nums[l] == val else 0
                l += 1
            
            if count == k:
                res += l + 1

        return res