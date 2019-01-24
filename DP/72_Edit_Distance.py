class Solution:
    def minDistance(self, s1, s2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(s1)
        n = len(s2)
        D = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            D[i][0] = i
        for j in range(n + 1):
            D[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                D[i][j] = min(D[i][j - 1] + 1,
                              D[i - 1][j] + 1,
                              D[i - 1][j - 1] + (s1[i - 1] != s2[j - 1]))
        return D[m][n]
