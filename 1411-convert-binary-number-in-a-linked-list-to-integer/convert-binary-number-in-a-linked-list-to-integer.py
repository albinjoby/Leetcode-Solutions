# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        arr = []
        temp = head
        while temp:
            arr.append(str(temp.val))
            temp = temp.next
        
        return int(''.join(arr),2)