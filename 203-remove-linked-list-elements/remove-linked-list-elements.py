# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        if not head: return None

        prev, curr = None, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next


        return head