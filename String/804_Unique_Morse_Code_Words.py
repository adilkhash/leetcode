import string

morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
               ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--",
               "-..-", "-.--", "--.."]

dictionary = dict(zip(string.ascii_letters, morse_codes))


class Solution:

    def transform(self, word):
        return ''.join([dictionary[char] for char in word])

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        unique = set()
        for word in words:
            unique.add(self.transform(word))
        return len(unique)


if __name__ == '__main__':
    print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
