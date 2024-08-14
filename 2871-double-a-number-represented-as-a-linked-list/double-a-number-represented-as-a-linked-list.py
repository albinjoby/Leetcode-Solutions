# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        s = ''
        temp = head

        while temp:
            s += str(temp.val)
            temp = temp.next
        
        nums = int(s)*2
        nums = str(nums)
        
        i = 0
        temp = head
        while i < len(nums):
            val = int(nums[i])
            if temp:
                temp.val = val
                if not temp.next and i < len(nums)-1:
                    temp.next = ListNode(0)
                temp = temp.next
            else:
                temp = ListNode(val)
            i += 1


        return head