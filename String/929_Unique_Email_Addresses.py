class Solution:

    def sanitize(self, email):
        name, host = email.split('@')
        new_name = []
        for char in name:
            if char == '.':
                continue
            if char == '+':
                break
            new_name.append(char)
        return '{}@{}'.format(''.join(new_name), host)

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for email in emails:
            unique.add(self.sanitize(email))
        return len(unique)


if __name__ == '__main__':
    assert Solution().numUniqueEmails(
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"
         ]
    ) == 2
