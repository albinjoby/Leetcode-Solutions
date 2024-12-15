class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 1

        return False