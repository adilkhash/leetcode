"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'LinkedList<{}>'.format(self.val)

    def __str__(self):
        return self.__repr__()


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        walker = head
        runner = head.next

        while walker != runner:
            if runner is None or runner.next is None:
                return
            walker = walker.next
            runner = runner.next.next

        walker = walker.next
        while walker != head:
            walker = walker.next
            head = head.next
        return walker


l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(3)
l2.next = l3
l4 = ListNode(3)
l3.next = l4
l4.next = None

print(Solution().detectCycle(l1))
