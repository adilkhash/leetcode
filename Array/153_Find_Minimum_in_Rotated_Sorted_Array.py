"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        if not nums:
            return -1

        while start <= end:
            mid = (start+end) // 2
            if nums[start] <= nums[mid] <= nums[end]:
                return nums[start]
            if nums[start] > nums[mid]:  # left is pivoted
                start += 1
            elif nums[mid] > nums[end]:  # right is pivoted
                start = mid + 1
