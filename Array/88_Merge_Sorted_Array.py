"""

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


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
