"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums):
        output = []
        prev = 1
        for i in nums:
            output.append(prev)
            prev = prev * i
        prev = 1
        for i in range(len(output)-1, -1, -1):
            output[i] = prev * output[i]
            prev = prev * nums[i]
        return output
