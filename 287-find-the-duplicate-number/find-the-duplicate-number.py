class Solution(object):
    def findDuplicate(self, nums):
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        