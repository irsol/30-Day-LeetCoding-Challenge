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
        # Counter for not zero elements 
        count_elem = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[count_elem] = nums[count_elem], nums[i]   # swap the positions of the elements
                count_elem += 1
        return nums