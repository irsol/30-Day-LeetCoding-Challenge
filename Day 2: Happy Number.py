# Day 2: Happy Number

# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the
# number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        
        while n != 1 and n not in s:
            s.add(n)
            sum = 0
            while n:
                sum += (n % 10) * (n % 10)
                n = int(n / 10)
            n = sum
        return n == 1