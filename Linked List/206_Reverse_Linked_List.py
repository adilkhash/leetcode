# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        current = head
        next = current.next
        current.next = None

        while next:
            old_next = next.next
            next.next = current
            current = next
            next = old_next
        return current
