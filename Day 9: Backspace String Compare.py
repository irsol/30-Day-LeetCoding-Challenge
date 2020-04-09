# Day 9: Backspace String Compare
# 
# Given two strings S and T, return if they are equal when both are typed into empty text editors.
# `#` means a backspace character.
# 
# Example 1:
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# 
# Example 2:
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# 
# Note:
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
