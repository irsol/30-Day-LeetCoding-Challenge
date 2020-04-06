# Day 6: Group Anagrams
#
# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
# ]
#
# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = {}

        for s in strs:
            t = "".join(sorted(s))
            if t in anagram:
                anagram[t].append(s)
            else:
                anagram[t] = [s]
        return list(anagram.values())
 


