class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """

        payload = []

        for i in range(11):
            for j in range(11):
                result = x ** i + y ** j
                if result <= bound:
                    payload.append(result)

        return list(set(payload))
