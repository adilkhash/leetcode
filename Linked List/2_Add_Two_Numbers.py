"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        y = 0
        p1 = l1
        p2 = l2
        head = ListNode(-1)
        cur = head

        while p1 or p2:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            s = sum((val1, val2)) + y
            y = 0
            if s >= 10:
                rem = s % 10  # остаток
                y = s // 10
                cur.next = ListNode(rem)
            else:
                cur.next = ListNode(s)
            cur = cur.next

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        if y:
            cur.next = ListNode(y)
        return head.next
