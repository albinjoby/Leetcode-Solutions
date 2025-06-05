class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        seen = set()
        for r in range(len(nums)):
            while r-l > k:
                seen.remove(nums[l])
                l += 1
            if nums[r] in seen:
                return True
            else:
                seen.add(nums[r])
        
        return False