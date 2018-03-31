"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        from collections import Counter

        if not tasks:
            return 0

        tasks = sorted(list(Counter(tasks).values()))

        total_cpu = 0
        while tasks[-1] > 0:
            i = 0
            p = len(tasks)-1
            while i <= n:
                if any(tasks) is False:
                    break
                if p < 0:
                    i += 1
                    total_cpu += 1
                    continue
                if tasks[p]:
                    tasks[p] -= 1
                    p -= 1
                i += 1
                total_cpu += 1
            tasks = sorted(tasks)
        return total_cpu
