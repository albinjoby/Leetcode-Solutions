# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        count = 0
        temp = head
        prev = None
        while temp:
            count += 1
            prev = temp
            temp = temp.next
        if k % count == 0: return head
        tail = prev
        target = count - (k % count)
        count = 0
        temp = head
        prev = None
        while temp and count != target:
            count += 1
            prev = temp
            temp = temp.next
        prev.next = None
        res = temp
        tail.next = head
        return res