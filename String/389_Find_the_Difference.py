from collections import Counter


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = Counter(s)
        t = Counter(t)
        for k, v in t.items():
            if k not in s:
                return k
            elif k in s and v > s[k]:
                return k


class Solution2:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)

        for i in range(len(t)):
            if i > len(s) - 1:
                return t[i]
            if s[i] != t[i]:
                return t[i]
