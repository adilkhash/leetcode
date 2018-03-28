"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        walker = head
        runner = head.next

        while walker != runner:
            if runner is None or runner.next is None:
                return False

            walker = walker.next
            runner = runner.next.next
        return True


l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(3)
l2.next = l3
l3.next = None

print(Solution().hasCycle(l1))
