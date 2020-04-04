# Day 4: Move Zeroes
#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pos_zero] = nums[pos_zero], nums[i]   # swap the positions of the elements
                i_zero += 1
        return nums