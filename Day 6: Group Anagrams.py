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
            # Sort every charachter in the string alphabetically
            t = "".join(sorted(s))
            # Check if sorted string t is a key in the anagram dictionary
            if t not in anagram:                
                anagram[t] = [s]                
            else: 
                anagram[t].append(s)
                  
        return list(anagram.values())
 


