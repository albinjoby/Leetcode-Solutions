class Solution(object):
    def rotate(self, nums, k):
        # Mod k by lenght so that we don't have to do extra rotations
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]