"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        zp = None
        cur = 0
        end = len(nums)-1
        while cur <= end:
            if nums[cur] == 0 and zp is None:
                zp = cur
                cur += 1
                continue

            if nums[cur] != 0 and zp is not None:
                nums[cur], nums[zp] = nums[zp], nums[cur]
                cur = zp
                zp = None
            cur += 1
