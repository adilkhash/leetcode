"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                return True

            while nums[l] == nums[mid] and l < mid:
                l += 1

            if nums[l] <= target < nums[mid]:  # left is sorted
                h = mid - 1
            elif nums[mid] < target <= nums[h]:  # right is sorted
                l = mid + 1
            elif nums[l] > nums[mid]:  # left is pivoted
                h = mid - 1
            else:  # right is pivoted
                l = mid + 1

        return False
