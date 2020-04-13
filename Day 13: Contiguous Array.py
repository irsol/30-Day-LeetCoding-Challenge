# Contiguous Array
# 
# Given a binary array, find the maximum length of a contiguous subarray with equal number of
# 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result, count = 0, 0
        table = {0: -1}

        for index, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if  count in table:
                result = max(result, index - table[count])
            else:
                table[count] = index
        return result
            
