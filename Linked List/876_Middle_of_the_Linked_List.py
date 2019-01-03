# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        current = head
        length = 1

        while current:
            if current.next:
                length += 1
            current = current.next

        mid = length // 2

        i = 0
        current = head
        while i < mid:
            current = current.next
            i += 1
        return current
