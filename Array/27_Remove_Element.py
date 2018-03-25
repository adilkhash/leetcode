"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        zp = None
        cur = 0
        end = len(nums)
        n = nums.count(val)
        while cur < end:
            if nums[cur] == val and zp is None:
                zp = cur
                cur += 1
                continue

            if nums[cur] != val and zp is not None:
                nums[cur], nums[zp] = nums[zp], nums[cur]
                cur = zp
                zp = None
            cur += 1
        return end-n
