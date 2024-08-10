# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        # Finding the length of the linkedlist
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1

        # Finding the left node
        left = head
        for i in range(1,k):
            left = left.next

        # Finding the right node
        count = length - k
        right = head
        for i in range(count):
            right = right.next

        #swap the values
        left.val, right.val = right.val, left.val

        return head