class Solution(object):
    def lengthOfLIS(self, nums):
        length = len(nums)
        res = [1]*length
        count = 1
        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    if res[j]+1 > res[i]:
                        res[i] = res[j]+1

        return max(res)
