# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        res = []
        for node in lists:
            while node:
                heapq.heappush(res,node.val)
                node = node.next

        dummy = ListNode()
        temp = dummy
        while res:
            temp.next = ListNode(heapq.heappop(res))
            temp = temp.next

        return dummy.next