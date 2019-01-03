class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        walker = runner = head
        # find mid
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next

        stack = []
        current = walker
        while current:
            stack.append(current.val)
            current = current.next

        walker = head
        while stack:
            val = stack.pop()
            if val != walker.val:
                return False
            walker = walker.next
        return True


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(3)
    l5 = ListNode(2)
    l6 = ListNode(1)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6

    print(Solution().isPalindrome(l1))
