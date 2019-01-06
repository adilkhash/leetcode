class Solution(object):

    def rotate(self, array, j):
        i = 0

        while i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    def find_max(self, array, size):
        mi = 0
        for i in range(0, size):
            if array[i] > array[mi]:
                mi = i
        return mi

    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        sorted_A = sorted(A)

        if A == sorted_A:
            return []

        current_size = len(A)
        vars = []

        while current_size > 1:
            k = self.find_max(A, current_size)
            if k != current_size - 1:
                self.rotate(A, k)
                self.rotate(A, current_size-1)
                vars += [k+1, current_size]
            current_size -= 1
        return vars
