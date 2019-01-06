class Solution:

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        index = [i for i, item in enumerate(s) if item in vowels]
        string = [s[i] for i in index][::-1]
        s = list(s)
        for i, item in enumerate(string):
            s[index[i]] = item
        return ''.join(s)


class Solution2:

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l = 0
        h = len(s) - 1
        s = list(s)

        while l < h:
            while l < h and s[l] not in vowels:
                l += 1
            while l < h and s[h] not in vowels:
                h -= 1
            s[l], s[h] = s[h], s[l]
            l += 1
            h -= 1

        return ''.join(s)
