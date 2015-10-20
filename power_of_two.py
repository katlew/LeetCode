
class Solution(object):
	def isPowerOfTwo(self, n):
        while n % 2 == 0 and n > 1
        	n /= 2
        return n == 1

"""
http://www.exploringbinary.com/ten-ways-to-check-if-an-integer-is-a-power-of-two-in-c/
http://www.programcreek.com/2014/07/leetcode-power-of-two-java/
Does a "bitwise and". 
Each bit of the output is 1 if the corresponding bit of 
x AND of y is 1, otherwise it's 0.
"""