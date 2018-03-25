"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        l = 0
        h = len(nums)-1
        while l <= h:
            mid = (l+h) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= target < nums[mid]:  # left is sorted
                h = mid - 1
            elif nums[mid] < target <= nums[h]:  # right is sorted
                l = mid + 1
            elif nums[mid] > nums[h]:  # right is pivoted
                l = mid + 1
            else:  # left is pivoted
                h = mid - 1

        return -1
