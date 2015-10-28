class Solution:
	def trailingZeroes(self, n):
		return self.numFiveFactorial(abs(n))
	def numFiveFactorial(self, n):
		result = 0
		while n != 0:
			result += n // 5
			print result
			n //= 5
			print n
		return result


"""
0! is 1

// Floor Division - 9//2 = 4.0
The division of operands where the 
result is the quotient in which the digits 
after the decimal point are removed.

For all integers, in form of (2^i)*(5^j)*x, i >= j. 
In other words, the number of pairs of 2 and 5 is 
determined by the number of j (min(i, j) = j). 
As a result, the number of tailing zeroes is 
j for the factorial result.

Time Limit Exceeded

class Solution(object):
    def trailingZeroes(self, n):
    	count = 0
    	num = self.factorial(n)
    	while num%10 == 0:
    		num/10
    		count += 1
    	return count

    def factorial(self,n):
    	result = 1
    	for i in xrange(2,n+1):
    		result *= i 
    	return result

"""