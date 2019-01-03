# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        while head.val == val:
            if head.next is None:
                return None
            head = head.next

        next = head.next
        prev = head

        while next:
            if next.val != val:
                prev = next
                next = next.next
            elif next.val == val:
                prev.next = next.next
                next = next.next

        return head
