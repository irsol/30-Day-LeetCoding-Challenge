# Day 3: Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# Example:
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        t = 0
        final_max = nums[0]
        for i in range(0, len(nums)):
            t = max(nums[i], nums[i]+t)
            if t > final_max:
                final_max = t
        return final_max



#        first_max_sum = 0
#        final_max_sum = 0

#        for n in range(0, len(nums)):
#            first_max_sum = first_max_sum + nums[n]
            #if first_max_sum < 0:
#                first_max_sum = 0
#            if final_max_sum < first_max_sum:
#                final_max_sum = first_max_sum
#        return final_max_sum
