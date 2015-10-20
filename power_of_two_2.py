
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
        	return False
        else:
        	return n & (n-1)

"""
http://www.exploringbinary.com/ten-ways-to-check-if-an-integer-is-a-power-of-two-in-c/
http://www.programcreek.com/2014/07/leetcode-power-of-two-java/
Does a "bitwise and". 
Each bit of the output is 1 if the corresponding bit of 
x AND of y is 1, otherwise it's 0.
"""