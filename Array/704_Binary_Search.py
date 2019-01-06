class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l+h) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= target < nums[mid]:
                h = mid - 1
            elif nums[mid] < target <= nums[h]:
                l = mid + 1
            else:
                return -1
