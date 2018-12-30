from collections import Counter


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        stones = Counter(S)

        number = 0
        for j in J:
            if j in stones:
                number += stones[j]
        return number


if __name__ == '__main__':
    assert Solution().numJewelsInStones('aA', 'aAAbbbb') == 3
    assert Solution().numJewelsInStones('A', 'AAbbb') == 2
    assert Solution().numJewelsInStones('Jajb', 'JJJajjjb') == 3+1+3+1
