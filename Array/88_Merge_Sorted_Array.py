class Solution:

    def sort(self, array, i):
        if len(array) > 1:
            while array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                i += 1
                if i >= len(array)-1:
                    break

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        l = 0
        r = 0
        while l <= m-1 and r <= n-1:
            if nums1[l] > nums2[r]:
                nums2[r], nums1[l] = nums1[l], nums2[r]
                self.sort(nums2, r)
                l += 1
            elif nums1[l] <= nums2[r]:
                l += 1

        for i in nums2:
            nums1[m] = i
            m += 1


if __name__:
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]

    m = 3
    n = 3

    Solution().merge(nums1, m, nums2, n)
    print(nums1)
